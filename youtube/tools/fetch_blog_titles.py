#!/usr/bin/env python3
"""
네이버 블로그 글 목록 수집기 — 로컬 실행용

원격 세션(Claude Code on the web)은 egress proxy에 막혀 외부 웹을 못 읽습니다.
이 스크립트는 사용자 컴퓨터에서 직접 돌려 글 목록을 뽑아내기 위한 것입니다.

사용법:
    python3 youtube/tools/fetch_blog_titles.py sh_forest303

출력:
    youtube/blog_posts.md    영상화 검토용 표 (그대로 붙여넣기 좋음)
    youtube/blog_posts.json  원본 데이터

표준 라이브러리만 사용합니다. 설치할 것 없음.
"""

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)
LIST_API = "https://blog.naver.com/PostTitleListAsync.naver"
RSS = "https://rss.blog.naver.com/{blog_id}.xml"


def get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Referer": "https://blog.naver.com/",
        "Accept": "*/*",
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", errors="replace")


def unquote(s):
    """네이버는 제목을 URL 인코딩 + '+' 공백으로 넘겨줍니다."""
    return urllib.parse.unquote_plus(s or "").strip()


def fetch_via_list_api(blog_id, max_pages=40):
    """
    PostTitleListAsync — 전체 글 목록을 페이지 단위로 반환.
    응답이 엄격한 JSON이 아니라(키에 따옴표 없음) 정규식으로 파싱합니다.
    """
    posts, seen = [], set()

    for page in range(1, max_pages + 1):
        qs = urllib.parse.urlencode({
            "blogId": blog_id,
            "viewdate": "",
            "currentPage": page,
            "categoryNo": "",
            "parentCategoryNo": "",
            "countPerPage": 30,
        })
        try:
            body = get(f"{LIST_API}?{qs}")
        except urllib.error.URLError as e:
            print(f"  ! {page}페이지 요청 실패: {e}", file=sys.stderr)
            break

        chunk = re.findall(
            r"logNo\s*:\s*'(\d+)'.*?title\s*:\s*'([^']*)'.*?addDate\s*:\s*'([^']*)'",
            body, re.S,
        )
        if not chunk:
            break

        new = 0
        for log_no, title, add_date in chunk:
            if log_no in seen:
                continue
            seen.add(log_no)
            new += 1
            posts.append({
                "logNo": log_no,
                "title": unquote(title),
                "date": unquote(add_date),
                "url": f"https://blog.naver.com/{blog_id}/{log_no}",
            })

        print(f"  {page}페이지 → 누적 {len(posts)}건")
        if new == 0:
            break

    return posts


def fetch_via_rss(blog_id):
    """폴백. 최근 글만 나오지만 목록 API가 막혔을 때 유용합니다."""
    body = get(RSS.format(blog_id=blog_id))
    posts = []
    for item in re.findall(r"<item>(.*?)</item>", body, re.S):
        def pick(tag):
            m = re.search(rf"<{tag}>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</{tag}>", item, re.S)
            return m.group(1).strip() if m else ""
        posts.append({
            "logNo": pick("link").rsplit("/", 1)[-1],
            "title": pick("title"),
            "date": pick("pubDate")[:16],
            "url": pick("link"),
        })
    return posts


def write_markdown(blog_id, posts, path):
    lines = [
        f"# blog.naver.com/{blog_id} — 글 목록 ({len(posts)}건)",
        "",
        "영상화 검토용. **적합도** 칸을 채워서 돌려주시면 스케줄에 반영합니다.",
        "",
        "- `A` 단독 롱폼 1편으로 충분",
        "- `B` 다른 글과 묶으면 1편",
        "- `C` 영상에는 부적합",
        "",
        "| # | 날짜 | 제목 | 적합도 |",
        "|---|---|---|---|",
    ]
    for i, p in enumerate(posts, 1):
        title = p["title"].replace("|", "\\|")
        lines.append(f"| {i} | {p['date']} | [{title}]({p['url']}) | |")
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    if len(sys.argv) < 2:
        print("사용법: python3 fetch_blog_titles.py <블로그ID>", file=sys.stderr)
        print("예:     python3 fetch_blog_titles.py sh_forest303", file=sys.stderr)
        return 2

    blog_id = sys.argv[1].strip().rstrip("/").split("/")[-1]
    print(f"블로그: {blog_id}")

    print("목록 API 시도...")
    try:
        posts = fetch_via_list_api(blog_id)
    except Exception as e:
        print(f"  ! 실패: {e}", file=sys.stderr)
        posts = []

    if not posts:
        print("RSS 폴백 시도...")
        try:
            posts = fetch_via_rss(blog_id)
        except Exception as e:
            print(f"  ! RSS도 실패: {e}", file=sys.stderr)

    if not posts:
        print("\n글을 하나도 못 가져왔습니다.", file=sys.stderr)
        print("블로그가 비공개이거나 ID가 다를 수 있습니다.", file=sys.stderr)
        print("브라우저에서 아래 주소가 열리는지 확인해 보세요:", file=sys.stderr)
        print(f"  https://blog.naver.com/{blog_id}", file=sys.stderr)
        return 1

    md = "youtube/blog_posts.md"
    js = "youtube/blog_posts.json"
    write_markdown(blog_id, posts, md)
    with open(js, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f"\n완료: {len(posts)}건")
    print(f"  {md}")
    print(f"  {js}")
    print("\n미리보기:")
    for p in posts[:10]:
        print(f"  {p['date']}  {p['title']}")
    if len(posts) > 10:
        print(f"  ... 외 {len(posts) - 10}건")
    return 0


if __name__ == "__main__":
    sys.exit(main())
