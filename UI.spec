# -*- mode: python -*-

block_cipher = None


a = Analysis(['UI.py', 'C:\\Users\\STU\\Desktop\\Strabismus_Program\\tensor\\label_image.py'],
             pathex=['C:\\Users\\STU\\Desktop\\Strabismus_Program'],
             binaries=[],
             datas=[('C:\\Users\\STU\\Desktop\\Strabismus_Program\\images', 'images'),('C:\\Users\\STU\\Desktop\\Strabismus_Program\\tensor', 'tensor')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='UI',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='UI')
