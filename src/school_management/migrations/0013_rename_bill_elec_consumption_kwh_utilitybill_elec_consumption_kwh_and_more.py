# Generated by Django 5.0 on 2024-02-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0012_utilitybill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilitybill',
            old_name='bill_elec_consumption_kwh',
            new_name='elec_consumption_kwh',
        ),
        migrations.RenameField(
            model_name='utilitybill',
            old_name='bill_gas_consumption_mmbtu',
            new_name='gas_consumption_therms',
        ),
        migrations.RenameField(
            model_name='utilitybill',
            old_name='bill_total_cost',
            new_name='peak_demand_kwh',
        ),
        migrations.RenameField(
            model_name='utilitybill',
            old_name='bill_water_consumption_gallons',
            new_name='total_electric_charges',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='CUI_co2_sqft',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='ECI_dollar_sqft',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='ECI_dollar_student',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='EUI_kbtu_sqft',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='EUI_kbtu_student',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='elec_consumption_kwh',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='emmissions_co2',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='gas_consumption_mmbtu',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='peak_demand_kw',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='renewables_kwh',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='total_consumption_mmbtu',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='total_cost_dollar',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='year_to_date_co2_savings',
        ),
        migrations.RemoveField(
            model_name='performancemetrics',
            name='year_to_date_kbtu_savings',
        ),
        migrations.RemoveField(
            model_name='utilitybill',
            name='meter_uid',
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='cui_scope1_gas_lbs_co2e_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='cui_scope1_gas_lbs_co2e_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='cui_scope2_elec_lbs_co2e_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='cui_scope2_elec_lbs_co2e_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='cui_total_lbs_co2e_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='cui_total_lbs_co2e_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='elec_energy_cost_index_dollar_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='elec_energy_cost_index_dollar_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='elec_energy_intensity_kwh_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='elec_energy_intensity_kwh_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='energy_cost_index_combined_dollar_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='energy_cost_index_combined_dollar_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='energy_use_intensity_combined_kbtu_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='energy_use_intensity_combined_kbtu_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='gas_energy_cost_index_dollar_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='gas_energy_cost_index_dollar_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='gas_energy_intensity_kbtu_sqft',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='gas_energy_intensity_kbtu_student',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='lbs_co2_per_lb_nh4',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='lbs_natural_gas_nh4',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='scope1_co2e_gas_lbs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='performancemetrics',
            name='scope2_co2e_elec_lbs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='utilitybill',
            name='meter_id',
            field=models.CharField(default='meter_id', max_length=100),
        ),
        migrations.AddField(
            model_name='utilitybill',
            name='off_peak_demand_kwh',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='utilitybill',
            name='service_agreement_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='utilitybill',
            name='total_gas_charges',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='utilitybill',
            name='bill_end_date',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='utilitybill',
            name='bill_start_date',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
