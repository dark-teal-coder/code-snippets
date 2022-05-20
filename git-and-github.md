# Compare Files using `diff`

```powershell
(base) PS C:\Users\Asus\Coding> compare-object (get-content .\file1.py) (get-content .\file2.py)

InputObject     SideIndicator
-----------     -------------
print("file 2") =>
print("file 1") <=

(base) PS C:\Users\Asus\Coding> diff (cat .\file1.py) (cat .\file2.py)

InputObject     SideIndicator
-----------     -------------
print("file 2") =>
print("file 1") <=

(base) PS C:\Users\Asus\Coding> diff (type .\file1.py) (type .\file2.py)

InputObject     SideIndicator
-----------     -------------
print("file 2") =>
print("file 1") <=

(base) PS C:\Users\Asus\Coding>
```
