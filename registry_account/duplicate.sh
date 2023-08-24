#!/bin/bash

# Đọc các tham số từ dòng lệnh

db_name=$1
db_clone_name=$2
admin_password=$3

# Đường dẫn đến thư mục chứa file backup
backup_dir="/opt/odoo/odoo-server/custom_addons/registry_account/db_base"

# Kiểm tra xem file backup có tồn tại không
if [ ! -f "$backup_dir/$db_clone_name.zip" ]; then
    echo "Backup file does not exist."
    exit 1
fi

# Restore
curl -F 'master_pwd='$admin_password \
    -F backup_file=@$backup_dir/$db_clone_name.zip \
    -F 'copy=true' \
    -F "name=\"$db_name\"" \
    http://localhost:8069/web/database/restore
