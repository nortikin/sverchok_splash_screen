import bpy
import sverchok
import importlib

"""
Скрипт для сбора документации
"""

print('СТАРТУЮ')
dict_htmls = {}
for i in dir(sverchok.nodes):
    for k in dir(getattr(sverchok.nodes,i)):
        name = []
        if not k.startswith('__') and not i.startswith('__'):
            print(i,k)
            try:
                k_mod = importlib.import_module(f'sverchok.nodes.{i}.{k}')
                for u in k_mod.__dict__:
                    a = getattr(k_mod,u)
                    try:
                        c = a.__bases__
                        for t in c:
                            if issubclass(t,bpy.types.Node):
                                name = [a.bl_idname]
                                label = [a.bl_label]
                                
                    except:
                        pass
            except:
                pass
            #name = [t for t in dir(k_mod) if t!='SverchCustomTreeNode' and t!='updateNode' and (t.endswith('Node') or t.lower().endswith('mk2') or t.lower().endswith('mk3') or t.lower().endswith('mk4') or t.lower().endswith('mk5') or t.lower().startswith('svviewer') or t.lower().endswith('viewer'))]
            if not name: continue
            #if name: name = name[0]
            #else: name = 'ПУСТОШЕСТВОВАНИЕ'
            dict_htmls[label[0]] = f'https://nortikin.github.io/sverchok/docs/nodes/{i}/{k}.html' # ' || '.join([label[0],name[0]])


for i,k in dict_htmls.items():
    bpy.data.texts['sverchok.log'].write(f'    "{i}":"{k}",\n')