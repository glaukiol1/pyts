find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find ./* | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find ./*/* | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find ./*/*/* | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find ./*/*/*/* | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# git add .
# git commit -m "auto-commit"
# git push