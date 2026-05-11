# Tutorial: crear un mòdul personalitzat a Odoo (versions recents)

Aquest tutorial és una guia ràpida per crear un mòdul propi compatible amb versions modernes d'Odoo (16/17/18).

## 1) Requisits previs

- Odoo instal·lat i funcionant
- Accés a una base de dades de proves
- Carpeta d'`addons` personalitzats (per exemple: `custom_addons`)
- Reinici del servidor Odoo quan modifiquis codi Python

## 2) Estructura base del mòdul

Exemple de nom del mòdul: `academy_course`

```bash
academy_course/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── course.py
├── views/
│   └── course_views.xml
└── security/
    └── ir.model.access.csv
```

## 3) Fitxer `__manifest__.py`

```python
{
    'name': 'Academy Course',
    'version': '1.0.0',
    'summary': 'Gestió bàsica de cursos',
    'author': 'El teu nom',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
    ],
    'installable': True,
    'application': True,
}
```

## 4) Inicialització de mòduls

`__init__.py` (arrel):

```python
from . import models
```

`models/__init__.py`:

```python
from . import course
```

## 5) Crear el model Python

`models/course.py`:

```python
from odoo import models, fields


class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = "Curs de l'acadèmia"

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Descripció')
    active = fields.Boolean(default=True)
```

## 6) Permisos d'accés

`security/ir.model.access.csv`:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_academy_course_user,academy.course.user,model_academy_course,base.group_user,1,1,1,1
```

## 7) Vistes i menú

`views/course_views.xml`:

```xml
<odoo>
    <record id="view_academy_course_tree" model="ir.ui.view">
        <field name="name">academy.course.tree</field>
        <field name="model">academy.course</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="active"/>
            </tree>
        </field>
    </record>

    <record id="view_academy_course_form" model="ir.ui.view">
        <field name="name">academy.course.form</field>
        <field name="model">academy.course</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="description"/>
                        <field name="active"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="action_academy_course" model="ir.actions.act_window">
        <field name="name">Cursos</field>
        <field name="res_model">academy.course</field>
        <field name="view_mode">tree,form</field>
    </record>

    <menuitem id="menu_academy_root" name="Acadèmia" sequence="10"/>
    <menuitem id="menu_academy_course" name="Cursos" parent="menu_academy_root" action="action_academy_course" sequence="20"/>
</odoo>
```

## 8) Instal·lar el mòdul

1. Afegeix la carpeta `custom_addons` a `addons_path` del fitxer de configuració d'Odoo.
2. Reinicia el servidor Odoo.
3. Activa el mode desenvolupador.
4. Ves a **Apps** i prem **Update Apps List**.
5. Busca `Academy Course` i instal·la'l.

## 9) Actualitzar canvis del mòdul

Quan modifiquis codi del mòdul:

```bash
odoo -u academy_course -d NOM_BASE_DE_DADES
```

## 10) Bones pràctiques per versions noves

- Defineix sempre permisos (`ir.model.access.csv`) abans d'instal·lar.
- Mantén separats models, vistes i dades de demo.
- Usa noms tècnics coherents (`academy.course`, `academy_course`).
- Afegeix traduccions i tests quan el mòdul creixi.
- Prova canvis en una base de dades de desenvolupament abans de producció.

---

Amb aquests passos ja tens un mòdul funcional i escalable per començar a personalitzar Odoo ERP.
