Set-Location examples
$files = Get-ChildItem -Directory 
for ($i = 0; $i -lt $files.Count; $i++) {
    $dir = $files[$i].FullName
    Set-Location $dir
    $Script = $dir + "\build_website.ps1"
    &$Script
    Set-Location ..
}
Set-Location ..
