[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [string]$Title,
  [string]$Slug,
  [string]$Year = (Get-Date).Year.ToString()
)

function Convert-ToSlug {
  param([string]$Text)
  $lower = $Text.ToLowerInvariant()
  $slug = $lower -replace '[^a-z0-9\s-]', ''
  $slug = $slug -replace '\s+', '-'
  $slug = $slug -replace '-+', '-'
  $slug = $slug.Trim('-')
  if ([string]::IsNullOrWhiteSpace($slug)) {
    return 'paper'
  }
  return $slug
}

if (-not $Slug) {
  $Slug = Convert-ToSlug -Text $Title
}

$root = Resolve-Path (Join-Path $PSScriptRoot '..')
$paperDir = Join-Path $root "papers\$Year\$Slug"

if (Test-Path $paperDir) {
  throw "Target already exists: $paperDir"
}

New-Item -ItemType Directory -Path $paperDir -Force | Out-Null
foreach ($sub in @('data', 'figures', 'exports')) {
  New-Item -ItemType Directory -Path (Join-Path $paperDir $sub) -Force | Out-Null
}

$templateDir = Join-Path $root 'templates'
$templates = @(
  'metadata.yml',
  'outline.md',
  'paper.md',
  'sources.md',
  'claims.csv',
  'notes.md',
  'checklist.md'
)

foreach ($t in $templates) {
  $src = Join-Path $templateDir $t
  $dst = Join-Path $paperDir $t
  Copy-Item $src $dst -Force
}

$tokens = @{
  '{{TITLE}}' = $Title
  '{{SLUG}}'  = $Slug
  '{{YEAR}}'  = $Year
  '{{DATE}}'  = (Get-Date -Format 'yyyy-MM-dd')
}

function Apply-Tokens {
  param(
    [string]$Path,
    [hashtable]$Tokens
  )
  $content = Get-Content $Path -Raw
  foreach ($key in $Tokens.Keys) {
    $content = $content.Replace($key, $Tokens[$key])
  }
  Set-Content -Path $Path -Value $content -Encoding UTF8
}

foreach ($t in $templates) {
  Apply-Tokens -Path (Join-Path $paperDir $t) -Tokens $tokens
}

Write-Host "Created $paperDir"
