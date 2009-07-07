import os
import shutil

def copytree_exists(src, dst, symlinks=False):
    if not os.path.exists(src):
        return

    names = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)

    errors = []
    for name in names:
        if name.startswith('CVS'):
            continue
        if name.startswith('.git'):
            continue
        if name.startswith('.svn'):
            continue

        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree_exists(srcname, dstname, symlinks)
            else:
                shutil.copy2(srcname, dstname)
        except (IOError, os.error), why:
            errors.append((srcname, dstname, why))
    if errors:
        print errors
