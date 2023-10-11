# Generated by Django 4.2.6 on 2023-10-11 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("diseases", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CGDCondition",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Gene",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hgnc_id", models.TextField(blank=True)),
                ("symbol", models.TextField(blank=True)),
                ("name", models.TextField(blank=True)),
                ("locus_group", models.TextField(blank=True)),
                ("locus_type", models.TextField(blank=True)),
                ("status", models.TextField(blank=True)),
                ("location", models.TextField(blank=True)),
                ("location_sortable", models.TextField(blank=True)),
                ("alias_symbol", models.TextField(blank=True)),
                ("alias_name", models.TextField(blank=True)),
                ("prev_symbol", models.TextField(blank=True)),
                ("prev_name", models.TextField(blank=True)),
                ("gene_family", models.TextField(blank=True)),
                ("gene_family_id", models.TextField(blank=True)),
                ("date_approved_reserved", models.TextField(blank=True)),
                ("date_symbol_changed", models.TextField(blank=True)),
                ("date_name_changed", models.TextField(blank=True)),
                ("date_modified", models.TextField(blank=True)),
                ("entrez_id", models.TextField(blank=True)),
                ("ensembl_gene_id", models.TextField(blank=True)),
                ("vega_id", models.TextField(blank=True)),
                ("ucsc_id", models.TextField(blank=True)),
                ("ena", models.TextField(blank=True)),
                ("refseq_accession", models.TextField(blank=True)),
                ("ccds_id", models.TextField(blank=True)),
                ("uniprot_ids", models.TextField(blank=True)),
                ("pubmed_id", models.TextField(blank=True)),
                ("mgd_id", models.TextField(blank=True)),
                ("rgd_id", models.TextField(blank=True)),
                ("lsdb", models.TextField(blank=True)),
                ("cosmic", models.TextField(blank=True)),
                ("omim_id", models.TextField(blank=True)),
                ("mirbase", models.TextField(blank=True)),
                ("homeodb", models.TextField(blank=True)),
                ("snornabase", models.TextField(blank=True)),
                ("bioparadigms_slc", models.TextField(blank=True)),
                ("orphanet", models.TextField(blank=True)),
                ("pseudogene_org", models.TextField(blank=True)),
                ("horde_id", models.TextField(blank=True)),
                ("merops", models.TextField(blank=True)),
                ("imgt", models.TextField(blank=True)),
                ("iuphar", models.TextField(blank=True)),
                ("kznf_gene_catalog", models.TextField(blank=True)),
                ("mamit_trnadb", models.TextField(blank=True)),
                ("cd", models.TextField(blank=True)),
                ("lncrnadb", models.TextField(blank=True)),
                ("enzyme_id", models.TextField(blank=True)),
                ("intermediate_filament_db", models.TextField(blank=True)),
                (
                    "diseases",
                    models.ManyToManyField(related_name="+", to="diseases.disease"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GeneCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("domain", models.CharField(blank=True, max_length=255)),
                ("name", models.TextField(blank=True)),
                ("go", models.CharField(max_length=255)),
                ("definition", models.TextField(blank=True)),
                ("genes", models.ManyToManyField(to="genes.gene")),
            ],
        ),
        migrations.CreateModel(
            name="GeneGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("genes", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Intervention",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Manifestation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gene",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="genes.gene"
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="genes.genecategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GoTerm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("goid", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("namespace", models.CharField(max_length=255)),
                ("level", models.CharField(max_length=255)),
                ("is_obsolete", models.BooleanField(default=True)),
                ("alt_ids", models.CharField(max_length=255)),
                (
                    "children",
                    models.ManyToManyField(
                        blank=True, related_name="children_go", to="genes.goterm"
                    ),
                ),
                (
                    "parents",
                    models.ManyToManyField(
                        blank=True, related_name="parents_go", to="genes.goterm"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GeneList",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                ("genes", models.TextField(blank=True)),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CGDEntry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("GENE", models.TextField(blank=True)),
                ("HGNC_ID", models.TextField(blank=True)),
                ("ENTREZ_GENE_ID", models.TextField(blank=True)),
                ("INHERITANCE", models.TextField(blank=True)),
                ("AGE_GROUP", models.TextField(blank=True)),
                ("ALLELIC_CONDITIONS", models.TextField(blank=True)),
                ("COMMENTS", models.TextField(blank=True)),
                ("INTERVENTION_RATIONALE", models.TextField(blank=True)),
                ("REFERENCES", models.TextField(blank=True)),
                (
                    "CONDITIONS",
                    models.ManyToManyField(blank=True, to="genes.cgdcondition"),
                ),
                (
                    "INTERVENTION_CATEGORIES",
                    models.ManyToManyField(blank=True, to="genes.intervention"),
                ),
                (
                    "MANIFESTATION_CATEGORIES",
                    models.ManyToManyField(blank=True, to="genes.manifestation"),
                ),
            ],
        ),
    ]
