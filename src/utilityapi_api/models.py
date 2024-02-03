from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.forms import JSONField
from .models import AuthorizationForm

STATUS_TYPES = (
        ('pending', 'Pending'),
        ('pending', 'Updated'),
        ('errored', 'Errored'),
    )
USER_STATUS_TYPES = (
    'active',
    'inactive',
)
UTILITY_ID = (
    ("ACE", "Atlantic City Electric"),
    ("AEPOHIO", "American Electric Power Ohio"),
    ("ALPower", "Alabama Power"),
    ("Ameren", "Ameren"),
    ("AppalachianPower", "Appalachian Power"),
    ("APS", "Arizona Public Service Company"),
    ("AustinEnergy", "Austin Energy"),
    ("BGE", "Baltimore Gas & Electric"),
    ("BLUEWATER", "Bluewater Power Distribution Corporation"),
    ("CEIC", "Cleveland Electric Illuminating Company"),
    ("ComEd", "Commonwealth Edison"),
    ("ConEd", "Consolidated Edison New York"),
    ("CONSUMERSENERGY", "Consumers Energy"),
    ("DEMO", "Demonstration Utility"),
    ("DEMOUTILITY", "Demo Utility"),
    ("DOMINION", "Dominion Energy"),
    ("Duke", "Duke Energy"),
    ("ESSEX", "Essex Powerlines"),
    ("EVRSRC", "Eversource Energy"),
    ("FCU", "Fort Collins Utilities"),
    ("FPL", "Florida Power and Light Company"),
    ("GAPower", "Georgia Power"),
    ("HECO", "Hawaii Electric"),
    ("IEDR", "Integrated Energy Data Resource Program"),
    ("JCPL", "Jersey Central Power and Light"),
    ("LADWP", "Los Angeles Department of Water & Power"),
    ("LAKEFRONT", "Lakefront Utilities Inc."),
    ("MonPower", "Mon Power"),
    ("NATGD", "National Grid"),
    ("NGNY", "National Grid New York"),
    ("NVE", "Nevada Energy"),
    ("NYSEG", "New York State Electric and Gas Corporation"),
    ("OhioEd", "Ohio Edison"),
    ("ORU", "Orange and Rockland Utilities"),
    ("PacPower", "Pacific Power Utilities"),
    ("PCE", "Peninsula Clean Energy"),
    ("PECO", "PECO Energy"),
    ("Penelec", "Penelec"),
    ("PEPCO", "Potomac Electric Power Company"),
    ("PG&E", "Pacific Gas and Electric"),
    ("PORTGE", "Portland General Electric"),
    ("PotomacEd", "Potomac Edison"),
    ("PPL", "Pennsylvania Power and Light"),
    ("PSEG", "Public Services Electric and Gas"),
    ("PSEGLI", "Public Services Electric and Gas - Long Island"),
    ("PSO", "Public Service Company of Oklahoma"),
    ("RMP", "Rocky Mountain Power"),
    ("SCE", "Southern California Edison"),
    ("SDG&E", "San Diego Gas and Electric"),
    ("SFPUC", "San Francisco Public Utilities Commission"),
    ("SMT", "Smart Meter Texas"),
    ("SMUD", "Sacramento Municipal Utility District"),
    ("SoCalGas", "Southern California Gas Company"),
    ("SRP", "Salt River Project"),
    ("SSMPUC", "PUC Distribution Inc."),
    ("SVCE", "Silicon Valley Clean Energy"),
    ("TEP", "Tucson Electric Power"),
    ("TEXGAS", "Texas Gas Service"),
    ("WashingtonGas", "Washington Gas"),
    ("WELLAND", "Welland Hydro-Electric System Corp"),
    ("WestPennPower", "West Penn Power"),
    ("XCEL", "Xcel Energy"),
)
# UNIVERSAL_METER_BLOCKS = (
#     ('base', )
# )
# BASE_METER_BLOCK

class TemplateSettings(models.Model):
    """
        This is the object representing a base form template settings for an authorization form. 
        The properties of these templates contain settings like what to do after a form is submitted, 
        who we should email notifications to, etc.
        docs here, https://utilityapi.com/docs/api/templates 
    """
    uid = models.CharField(primary_key=True, max_length=100, blank=True, null=True)
    created = models.CharField(max_length=100, blank=True, null=True)
    updated = models.CharField(max_length=100, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_uid = models.CharField(max_length=100, blank=True, null=True)
    disabled = models.BooleanField(default=False)
    portal = models.CharField(max_length=100, blank=True, null=True)
    base_url = models.URLField()
    redirect_uris = ArrayField(models.URLField(), default=list, blank=True, help_text="Whitelist of locations to redirect the user after authorization is complete.")
    company_logo = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_email = models.CharField(max_length=100, blank=True, null=True)


class Authorization(models.Model):
    """ This is the object representing a customer (i.e. utility account holder) 
        authorization to share data with a user. This object contains the customer authorization 
        and access information for the utility account. Docs, https://utilityapi.com/docs/api/authorizations
    """
    uid = models.CharField(primary_key=True, max_length=100, blank=True, null=True)
    created = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_signature = JSONField(default=dict)
    declined = models.CharField(max_length=100, blank=True, null=True)
    is_declined = models.BooleanField(default=False)
    expired = models.CharField(max_length=100, blank=True, null=True)
    is_expired = models.BooleanField(default=False)
    exports_list = JSONField(default=list)
    form_uid = models.ForeignKey(AuthorizationForm, on_delete=models.CASCADE)
    template_uid = models.ForeignKey(TemplateSettings, on_delete=models.CASCADE)
    referrals = ArrayField(models.CharField(max_length=100), default=list, blank=True, help_text="List of referral codes that have been used to access this form.")
    is_archived = models.BooleanField(default=False)
    is_test = models.BooleanField(default=False)
    notes = JSONField(default=list)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    revoked = models.CharField(max_length=100, blank=True, null=True)
    is_revoked = models.BooleanField(default=False)
    scope =  JSONField(default=dict)
    status = models.CharField(max_length=100, choices=STATUS_TYPES, default='pending')
    status_message = models.CharField(max_length=100, blank=True, null=True)
    status_ts =  models.CharField(max_length=100, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_uid = models.CharField(max_length=100, blank=True, null=True)
    user_status = models.CharField(max_length=100, choices=USER_STATUS_TYPES, default='active')
    utility = models.CharField(max_length=100, choices=UTILITY_ID, default='active')


class AuthorizationForm(models.Model):
    """
        This is the object representing an authorization form that has be generated and can 
        be submitted by a customer. This object contains a link to the form and any prefill 
        information that's included by default.docs, https://utilityapi.com/docs/api/forms 
    """
    uid = models.CharField(primary_key=True, max_length=100, blank=True, null=True)
    created = models.CharField(max_length=100, blank=True, null=True)
    updated = models.CharField(max_length=100, blank=True, null=True)
    template_uid = models.ForeignKey(TemplateSettings, on_delete=models.CASCADE)
    authorization_uid = models.ForeignKey(Authorization, on_delete=models.CASCADE)
    is_archived = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_uid = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField()
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    # utility = models.CharField(max_length=100, choices=UTILITY_ID, default='active') get this from Authorization model
    scope = JSONField(default=dict)


class Meters(models.Model):
    """ 
        This is the object representing a utility meter or similar service., docs, https://utilityapi.com/docs/api/meters
    """
    uid = models.CharField(primary_key=True, max_length=100, blank=True, null=True)
    authorization_uid = models.ForeignKey(Authorization, on_delete=models.CASCADE)
    created = models.CharField(max_length=100, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_uid = models.CharField(max_length=100, blank=True, null=True)
    is_archived = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)
    notes = JSONField(default=list)
    status = models.CharField(max_length=100, choices=STATUS_TYPES, default='pending')
    status_message = models.CharField(max_length=100, blank=True, null=True)
    status_ts = models.CharField(max_length=100, blank=True, null=True)
    ongoing_monitoring = JSONField(default=dict)
    utility = models.CharField(max_length=100, choices=UTILITY_ID, default='active')
    bill_count = models.IntegerField()
    bill_coverage = models.JSONField(default=list)
    bill_sources = JSONField(default=list)
    interval_count = models.IntegerField()
    exports_list = JSONField(default=list)
    # blocks = JSONField(default=list)
    # {block_type} = 
    is_expanded = models.BooleanField(default=False)


class Bill(models.Model):
    """
        This is the object representing utility bill. This object contains bill data, 
        including usage and pricing. Docs, https://utilityapi.com/docs/api/bills
    """
    uid = models.CharField(primary_key=True, max_length=100, blank=True, null=True)
    meter_uid = models.ForeignKey(Meters, on_delete=models.CASCADE)
    authorization_uid = models.ForeignKey(Authorization, on_delete=models.CASCADE)
    created = models.CharField(max_length=100, blank=True, null=True)
    updated = models.CharField(max_length=100, blank=True, null=True)
    notes = JSONField(default=list)
    utility = models.CharField(max_length=100, choices=UTILITY_ID, default='active')
    # blocks = 
    # {block_type}


class Intervals(models.Model):
    """
        This is the object representing utility interval. This object contains interval kwh data.
        docs, https://utilityapi.com/docs/api/intervals
    """
    uid = models.CharField(primary_key=True, max_length=100, blank=True, null=True)
    meter_uid = models.ForeignKey(Meters, on_delete=models.CASCADE)
    authorization_uid = models.ForeignKey(Authorization, on_delete=models.CASCADE)
    created = models.CharField(max_length=100, blank=True, null=True)
    updated = models.CharField(max_length=100, blank=True, null=True)
    notes = JSONField(default=list)
    utility = models.CharField(max_length=100, choices=UTILITY_ID, default='active')
    # blocks = 
    # {block_type}


# class Files(models.Model):
#     """
#         This is an open-ended endpoint that is a catchall for raw files and export downloads 
#         that are linked in the normal API endpoints. Files under this endpoint must be accessed 
#         directly (i.e. you can't list files visible to you). These requests are still authenticated, 
#         which means they require an api token. Docs, https://utilityapi.com/docs/api/files
#     """
    

class Events(models.Model):
    """
        This is the object representing an an event notification that has been triggered by a 
        task or update to other parts of the API. If you have configured your settings to receive 
        webhooks, these are the objects that are pushed to your server. docs https://utilityapi.com/docs/api/events
    """
    uid = models.CharField(primary_key=True, max_length=100, blank=True, null=True)
    # type = 
    ts = models.CharField(max_length=100, blank=True, null=True)
    # delivery_method = 
    delivery_target = models.URLField()
    is_delivered = models.BooleanField(default=False)



# class Accounting
# https://utilityapi.com/docs/api#accounting 






