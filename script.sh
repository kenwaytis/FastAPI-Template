#!/bin/bash

# 交互式输入 Project Name
read -p "Project Name: " project_name

# 判断首字母是否大写
if [[ $project_name =~ ^[A-Z] ]]; then
  upper_case=true
else
  upper_case=false
fi

# 函数：替换文件内容
replace_content() {
  local file=$1
  if $upper_case; then
    sed -i "s/{{Tmp}}/$project_name/g" "$file"
    sed -i "s/{{tmp}}/${project_name,}/g" "$file"
  else
    sed -i "s/{{tmp}}/$project_name/g" "$file"
    sed -i "s/{{Tmp}}/${project_name^}/g" "$file"
  fi
}

# 函数：替换文件名
replace_filename() {
  local file=$1
  local dir=$(dirname "$file")
  local filename=$(basename "$file")
  if $upper_case; then
    new_filename=$(echo "$filename" | sed "s/tmp/${project_name,}/g")
  else
    new_filename=$(echo "$filename" | sed "s/tmp/$project_name/g")
  fi
  mv "$file" "$dir/$new_filename"
}

# 递归遍历文件夹
traverse_directory() {
  local dir=$1
  for file in "$dir"/*; do
    if [ -d "$file" ]; then
      traverse_directory "$file"
    else
      replace_content "$file"
      replace_filename "$file"
    fi
  done
}

# 开始遍历当前文件夹
traverse_directory "."

echo "Fastapi template project is established"
