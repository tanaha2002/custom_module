param(
    [string]$db_name,
    [string]$db_clone_name,
    [string]$admin_password,
    [string]$user_password,
    [string]$login
)

# Đường dẫn đến thư mục chứa file backup
$backup_dir = "odoo/custom_addons/registry_account/db_base"

# Kiểm tra xem file backup có tồn tại không
if (-Not (Test-Path "$backup_dir\$db_clone_name.zip")) {
    Write-Output "Backup file does not exist."
    Exit 1
}

# Restore
$restore_point = $db_clone_name
Invoke-RestMethod -Uri "http://localhost:8069/web/database/restore" -Method Post -FormData @{
    master_pwd = $admin_password
    name = $db_name
    copy = "true"
    restore_point = $restore_point
    file = Get-Item "$backup_dir\$db_clone_name.zip"
}