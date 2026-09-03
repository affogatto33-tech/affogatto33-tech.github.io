<#
.SYNOPSIS
    네이버 블로그 글 목록 수집기 — PowerShell 버전 (파이썬 불필요)

.DESCRIPTION
    윈도우에 기본 내장된 PowerShell만으로 동작합니다. 설치할 것 없음.
    파이썬이 없거나 'python3' 명령이 없는 환경을 위한 대안입니다.

.EXAMPLE
    .\youtube\tools\Fetch-BlogTitles.ps1 sh_forest303
#>

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$BlogId,

    [int]$MaxPages = 40
)

$ErrorActionPreference = 'Stop'

# 윈도우 기본값이 TLS 1.0인 경우가 있어 명시적으로 올립니다
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
      '(KHTML, like Gecko) Chrome/125.0 Safari/537.36'

function Get-Text([string]$Url) {
    $r = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 20 -Headers @{
        'User-Agent' = $UA
        'Referer'    = 'https://blog.naver.com/'
    }
    # 응답이 UTF-8이므로 원본 바이트에서 직접 디코딩합니다
    return [Text.Encoding]::UTF8.GetString($r.RawContentStream.ToArray())
}

function Convert-NaverTitle([string]$S) {
    # 네이버는 제목을 URL 인코딩 + '+' 공백으로 넘겨줍니다.
    # WebUtility.UrlDecode 가 '+' 를 공백으로 처리해 줍니다.
    return [Net.WebUtility]::UrlDecode($S).Trim()
}

Write-Host "블로그: $BlogId"
Write-Host "목록 API 시도..."

$posts = New-Object System.Collections.ArrayList
$seen  = New-Object System.Collections.Generic.HashSet[string]

for ($page = 1; $page -le $MaxPages; $page++) {
    $url = "https://blog.naver.com/PostTitleListAsync.naver" +
           "?blogId=$BlogId&viewdate=&currentPage=$page" +
           "&categoryNo=&parentCategoryNo=&countPerPage=30"

    try {
        $body = Get-Text $url
    }
    catch {
        Write-Warning "  $page 페이지 요청 실패: $($_.Exception.Message)"
        break
    }

    $rx = [regex]"(?s)logNo\s*:\s*'(\d+)'.*?title\s*:\s*'([^']*)'.*?addDate\s*:\s*'([^']*)'"
    $found = $rx.Matches($body)
    if ($found.Count -eq 0) { break }

    $new = 0
    foreach ($m in $found) {
        $logNo = $m.Groups[1].Value
        if (-not $seen.Add($logNo)) { continue }
        $new++
        [void]$posts.Add([pscustomobject]@{
            logNo = $logNo
            title = Convert-NaverTitle $m.Groups[2].Value
            date  = Convert-NaverTitle $m.Groups[3].Value
            url   = "https://blog.naver.com/$BlogId/$logNo"
        })
    }

    Write-Host "  $page 페이지 → 누적 $($posts.Count)건"
    if ($new -eq 0) { break }
}

if ($posts.Count -eq 0) {
    Write-Host ""
    Write-Warning "글을 하나도 못 가져왔습니다."
    Write-Host "블로그가 비공개이거나 ID가 다를 수 있습니다." -ForegroundColor Yellow
    Write-Host "브라우저에서 아래가 열리는지 확인해 보세요:" -ForegroundColor Yellow
    Write-Host "  https://blog.naver.com/$BlogId" -ForegroundColor Yellow
    exit 1
}

# 출력 경로 (저장소 루트 기준)
$root  = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$mdOut = Join-Path $root 'youtube\blog_posts.md'
$jsOut = Join-Path $root 'youtube\blog_posts.json'

$lines = New-Object System.Collections.ArrayList
[void]$lines.Add("# blog.naver.com/$BlogId — 글 목록 ($($posts.Count)건)")
[void]$lines.Add("")
[void]$lines.Add("영상화 검토용. **적합도** 칸을 채워서 돌려주시면 스케줄에 반영합니다.")
[void]$lines.Add("")
[void]$lines.Add("- ``A`` 단독 롱폼 1편으로 충분")
[void]$lines.Add("- ``B`` 다른 글과 묶으면 1편")
[void]$lines.Add("- ``C`` 영상에는 부적합")
[void]$lines.Add("")
[void]$lines.Add("| # | 날짜 | 제목 | 적합도 |")
[void]$lines.Add("|---|---|---|---|")

$i = 0
foreach ($p in $posts) {
    $i++
    $t = $p.title -replace '\|', '\|'
    [void]$lines.Add("| $i | $($p.date) | [$t]($($p.url)) | |")
}
[void]$lines.Add("")

# BOM 없는 UTF-8 로 저장 (Out-File -Encoding utf8 은 PS 5.1 에서 BOM 을 붙입니다)
$utf8 = New-Object Text.UTF8Encoding $false
[IO.File]::WriteAllText($mdOut, ($lines -join "`r`n"), $utf8)
[IO.File]::WriteAllText($jsOut, ($posts | ConvertTo-Json -Depth 3), $utf8)

Write-Host ""
Write-Host "완료: $($posts.Count)건" -ForegroundColor Green
Write-Host "  $mdOut"
Write-Host "  $jsOut"
Write-Host ""
Write-Host "미리보기:"
$posts | Select-Object -First 10 | ForEach-Object {
    Write-Host "  $($_.date)  $($_.title)"
}
if ($posts.Count -gt 10) {
    Write-Host "  ... 외 $($posts.Count - 10)건"
}
