# -*- coding: utf-8 -*-
"""
Crispy forms layouts
"""
import re

from django import forms
from django.utils.translation import ugettext as _

from django.utils.text import normalize_newlines
from django.utils.html import escape

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import UneditableField
from crispy_forms_foundation.layout import TEMPLATE_PACK, Layout, Row, Column, HTML, Div, Fieldset, Field, ButtonHolder, ButtonHolderPanel, ButtonGroup, Panel, Submit

def SimpleRowColumn(field, *args, **kwargs):
    """
    Shortcut for simple row with only a full column
    """
    if isinstance(field, basestring):
        field = Field(field, *args, **kwargs)
    return Row(
        Column(field),
    )

class SourceTextField(UneditableField):
    """
    Layout object for rendering template field value as html and a hidden input
    
    Field value rendering is at your charge in the template (default is to use 
    Django's 'linebreaks' filter)
    """
    template = "po_projects/input_as_text.html"
    
    def linebreaks(self, value, autoescape=True):
        """
        Converts newlines into <p> and <br />s. Additionnaly add a carriage return 
        character before each simple line break.
        
        Taken from ``django.utils.html.linebreaks`` then modified to fit needs.
        """
        value = normalize_newlines(value)
        paras = re.split('\n{2,}', value)
        if autoescape:
            paras = ['<p>%s</p>' % escape(p).replace('\n', u'<span class="explicit_cr">↵</span><br />') for p in paras]
        else:
            paras = ['<p>%s</p>' % p.replace('\n', u'<span class="explicit_cr">↵</span><br />') for p in paras]
        return '\n\n'.join(paras)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['source_content'] = self.linebreaks(form.instance.template.message)

        return super(SourceTextField, self).render(form, form_style, context, template_pack=TEMPLATE_PACK)


def project_helper(instance=None, form_tag=True):
    """
    Project form helper
    """
    helper = FormHelper()
    helper.form_action = '.'
    helper.attrs = {'data_abide': ''}
    helper.form_tag = form_tag
    
    fields = [SimpleRowColumn('name', css_class='small-12')]
    if not instance:
        fields.append(SimpleRowColumn('slug', css_class='small-12'))
    fields = fields+[
        SimpleRowColumn('domain', css_class='small-12'),
        SimpleRowColumn('description', css_class='small-12'),
        SimpleRowColumn('po_file', css_class='small-12'),
    ]
    
    helper.layout = Layout(
        Fieldset(
            '',
            *fields,
            css_class='no-legend'
        ),
        ButtonHolderPanel(
            Submit(
                'submit',
                _('Save'),
            ),
            css_class='text-right',
        )
    )
    
    return helper


def inline_catalog_helper(instance=None, form_tag=True):
    """
    Form helper to create a new catalog
    """
    helper = FormHelper()
    helper.form_action = '.'
    helper.form_class = "hide-label"
    helper.attrs = {'data_abide': ''}
    helper.form_tag = form_tag
    
    # Build the full layout
    helper.layout = Layout(
        Row(
            Field(
                'locale', 
                placeholder=_("Type a locale like 'fr'"), 
                wrapper_class='small-10 columns'
            ),
            Column(
                Submit(
                    'submit',
                    _('Create'),
                    css_class='postfix',
                ),
                css_class='small-2'
            ),
            css_class='collapse postfix-radius',
        )
    )
    
    return helper

def catalog_update_helper(instance=None, form_tag=True):
    """
    Form helper to update a catalog
    """
    helper = FormHelper()
    helper.form_action = '.'
    helper.attrs = {'data_abide': ''}
    helper.form_tag = form_tag
    
    helper.layout = Layout(
        Fieldset(
            '',
            Row(
                Column('locale', css_class='small-12'),
                Column('po_file', css_class='small-12'),
            ),
            css_class='no-legend',
        ),
            ButtonHolderPanel(
                Submit(
                    'submit',
                    _('Save'),
                    css_class='small',
                ),
                css_class='text-right',
            )
    )
    
    return helper


def translation_helper(instance=None, prefix='', form_tag=False):
    """
    Catalog's message translations form layout helper
    """
    helper = FormHelper()
    helper.form_action = '.'
    helper.form_class = 'catalog-messages-form'
    helper.form_tag = form_tag
    helper.disable_csrf = True
    helper.render_required_fields = True
    
    row_css_classes = ['message-row', 'clearfix']
    if instance is not None and instance.fuzzy:
        row_css_classes.append('fuzzy')
    elif instance is not None and not instance.message:
        row_css_classes.append('disabled empty')
    else:
        row_css_classes.append('enabled')
        
    anchor_link = ''
    if prefix:
        prefix_id = int(prefix[len('form-'):]) + 1
        anchor_link = '<a href="#item-{0}" id="item-{0}">#{0}</a>'.format(prefix_id)
    
    helper.layout = Layout(
        Div(
            Div(
                HTML(anchor_link),
                css_class='anchor',
            ),
            Div(
                Div(
                    'fuzzy',
                    css_class='fuzzy-field',
                ),
                Div(
                    Div(
                        SourceTextField('template'),
                        css_class='flex-item source',
                    ),
                    Field(
                        'message',
                        placeholder=_("Type your translation here else the original text will be used"),
                        wrapper_class='flex-item edit',
                    ),
                    css_class='flex-container',
                ),
                css_class=' '.join(row_css_classes),
            ),
            css_class='row-wrapper',
        ),
    )
    #helper.add_input(Submit('submit', 'Submit'))
    
    return helper
