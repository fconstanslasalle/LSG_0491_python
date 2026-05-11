Aquí tens una guia detallada en format Markdown per crear un mòdul personalitzat a Odoo, cobrint les especificitats de les versions 15, 16 i 17.

Tutorial: Creació d'un Mòdul Personalitzat a Odoo (v15, v16, v17)
Aquest tutorial et guiarà en la creació d'un mòdul bàsic anomenat gestio_tasques. Tot i que l'estructura base és gairebé idèntica en les darreres tres versions, destacarem les diferències clau on calgui.

1. Prerequisits
Odoo instal·lat (v15, v16 o v17).

Python 3.8+ (v15/v16) o Python 3.10+ (v17).

PostgreSQL instal·lat i configurat.

2. Estructura del Mòdul
Primer, crea la carpeta del teu mòdul dins del directori d' addons personalitzats:

Plaintext
gestio_tasques/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── tasca.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── tasca_views.xml
3. El Fitxer de Manifest (__manifest__.py)
Aquest fitxer conté la metainformació del mòdul.

Python
# -*- coding: utf-8 -*-
{
    'name': 'Gestió de Tasques',
    'version': '17.0.1.0.0',  # Canvia a 16.0 o 15.0 segons la teva versió
    'category': 'Productivity',
    'summary': 'Mòdul senzill per gestionar tasques diàries',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tasca_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
4. Definició del Model (models/tasca.py)
Crearem un model senzill per guardar les nostres tasques.

Python
from odoo import models, fields

class Tasca(models.Model):
    _name = 'gestio.tasca'
    _description = 'Tasca de l’usuari'

    name = fields.Char(string='Títol', required=True)
    description = fields.Text(string='Descripció')
    is_done = fields.Boolean(string='Feta?', default=False)
    priority = fields.Selection([
        ('0', 'Baixa'),
        ('1', 'Mitjana'),
        ('2', 'Alta')
    ], string='Prioritat', default='1')
No oblidis importar el fitxer al models/__init__.py:

Python
from . import tasca
I a l'arrel __init__.py:

Python
from . import models
5. Seguretat (security/ir.model.access.csv)
Sense aquest fitxer, el model no serà visible per als usuaris (excepte l'administrador en mode debug en versions antigues).

Fragmento de código
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_gestio_tasca,access_gestio_tasca,model_gestio_tasca,base.group_user,1,1,1,1
6. Creació de la Vista (views/tasca_views.xml)
Definim com es veurà el mòdul a la interfície.

XML
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_tasca_tree" model="ir.ui.view">
        <field name="name">gestio.tasca.tree</field>
        <field name="model">gestio.tasca</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="priority"/>
                <field name="is_done"/>
            </tree>
        </field>
    </record>

    <record id="view_tasca_form" model="ir.ui.view">
        <field name="name">gestio.tasca.form</field>
        <field name="model">gestio.tasca</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="priority"/>
                        <field name="description"/>
                        <field name="is_done"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="action_gestio_tasques" model="ir.actions.act_window">
        <field name="name">Tasques</field>
        <field name="res_model">gestio.tasca</field>
        <field name="view_mode">tree,form</field>
    </record>

    <menuitem id="menu_tasques_root" name="Tasques" sequence="10"/>
    <menuitem id="menu_tasques_llista" name="La meva llista" parent="menu_tasques_root" action="action_gestio_tasques"/>
</odoo>
7. Diferències entre Versions
Odoo 15
Interfície: Utilitza l'estil clàssic de la versió 15.

Codi: Encara és molt comú veure l'ús d'atributs states en els camps (que es va simplificar en versions posteriors).

Odoo 16
Comandaments: S'introdueix la barra de comandaments ràpids (Ctrl+K).

Vistes: S'elimina definitivament l'atribut attrs en favor de expressions directes a XML (ex: invisible="is_done == True"). Nota: Tot i que a la v16 attrs encara funciona, es recomana el nou format.

Odoo 17
Interfície "Milk": Canvi radical de disseny. Les icones són noves i el mode fosc és natiu.

Atributs XML: L'atribut attrs i states han estat eliminats totalment del nucli. Ara s'utilitzen atributs com invisible, readonly i required directament amb lògica booleana.

Exemple v17: <field name="description" invisible="is_done"/>

Arquitectura: Més ús de components OWL (Odoo Web Library) en el frontend.

8. Com instal·lar el mòdul
Reinicia el servidor d'Odoo carregant el directori d'addons:

Bash
./odoo-bin -c odoo.conf -u gestio_tasques
Activa el Mode Desenvolupador a Odoo (Ajustos -> Activar mode desenvolupador).

Vés a Aplicacions -> Actualitzar llista d'aplicacions.

Cerca "Gestió de Tasques", elimina el filtre "Aplicacions" si és necessari, i prem Instal·lar.

Consell Pro:
Si vols crear l'estructura ràpidament, pots fer servir la comanda scaffold des del terminal:

Bash
python3 odoo-bin scaffold el_teu_modul addons_path/
Això crearà totes les carpetes i fitxers __init__ automàticament.