# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0080_auto_20160420_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('abstractfilterpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='v1.AbstractFilterPage')),
                ('content', wagtail.wagtailcore.fields.StreamField([(b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))]))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.abstractfilterpage',),
        ),
        migrations.AlterField(
            model_name='abstractfilterpage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'item_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'Amicus Brief', ((b'us-supreme-court', b'U.S. Supreme Court'), (b'fed-circuit-court', b'Federal Circuit Court'), (b'fed-district-court', b'Federal District Court'), (b'state-court', b'State Court'))), (b'Blog', ((b'at-the-cfpb', b'At the CFPB'), (b'policy_compliance', b'Policy & Compliance'), (b'data-research-reports', b'Data, research & reports'), (b'info-for-consumers', b'Info for consumers'))), (b'Enforcement action', ((b'fed-district-case', b'Federal District Court Case'), (b'admin-filing', b'Administrative Filing'))), (b'Final Rule', ((b'interim-final-rule', b'Interim Final Rule'), (b'final-rule', b'Final Rule'))), (b'FOIA Frequently Requested Record', ((b'report', b'Report'), (b'log', b'Log'), (b'record', b'Record'))), (b'Implementation Resource', ((b'compliance-aid', b'Compliance aid'), (b'official-guidance', b'Official guidance'))), (b'Newsroom', ((b'op-ed', b'Op-Ed'), (b'press-release', b'Press Release'), (b'speech', b'Speech'), (b'testimony', b'Testimony'))), (b'Notice and Opportunity for Comment', ((b'notice-proposed-rule', b'Advanced Notice of Proposed Rulemaking'), (b'proposed-rule', b'Proposed Rule'), (b'interim-final-rule-2', b'Interim Final Rule'), (b'request-comment-info', b'Request for Comment or Information'), (b'proposed-policy', b'Proposed Policy'), (b'intent-preempt-determ', b'Intent to make Preemption Determination'), (b'info-collect-activity', b'Information Collection Activities'), (b'notice-privacy-act', b'Notice related to Privacy Act'))), (b'Research Report', ((b'consumer-complaint', b'Consumer Complaint'), (b'super-highlight', b'Supervisory Highlights'), (b'data-point', b'Data Point'), (b'industry-markets', b'Industry and markets'), (b'consumer-edu-empower', b'Consumer education and empowerment'), (b'to-congress', b'To Congress'))), (b'Rule under development', ((b'notice-proposed-rule-2', b'Advanced Notice of Proposed Rulemaking'), (b'proposed-rule-2', b'Proposed Rule')))])), (b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'date', wagtail.wagtailcore.blocks.DateTimeBlock(required=False)), (b'has_social', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Whether to show the share icons or not.', required=False))])), (b'blog_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'date', wagtail.wagtailcore.blocks.DateTimeBlock(required=False)), (b'has_social', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Whether to show the share icons or not.', required=False))]))], blank=True),
        ),
        migrations.CreateModel(
            name='NewsroomPage',
            fields=[
                ('blogpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='v1.BlogPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.blogpage',),
        ),
    ]
