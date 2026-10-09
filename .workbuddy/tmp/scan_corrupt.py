import os, sys

root = r"D:\code\bailian\new-api\web\node_modules"
bad = []
checked = 0
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        p = os.path.join(dirpath, fn)
        try:
            st = os.stat(p)
        except OSError:
            continue
        if st.st_size == 0:
            continue
        checked += 1
        try:
            with open(p, "rb") as f:
                head = f.read(4096)
        except OSError:
            continue
        if head and head.count(b"\x00") == len(head):
            bad.append((p, st.st_size))

print("checked:", checked)
print("corrupt(all-null head):", len(bad))
for p, s in bad[:200]:
    print(s, p)
