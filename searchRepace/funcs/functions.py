import os


def search_replace(s1, r1):
    command = os.system(f"wp search-replace '{s1}' '{r1}' --all-tables --precise --recurse-objects")
    return "Process completed successfully. "


def css_search_replace(s1, r1):
    command = os.system(f"egrep -lRZ '{s1}' . | xargs -0 -l sed -i -e 's/{s1}/{r1}/g' *.css ")
 

def db_backup_creation():
    command = os.system("wp db export backup.sql")


def cache_flush():
    command = os.system("wp cache flush --skip-plugins --skip-themes; wp sg purge --skip-themes; wp rewrite flush --skip-plugins --skip-themes; wp transient delete --expired --skip-plugins --skip-themes; rm -rf wp-content/cache/*; rm -rf ~/.opcache/*")
    return "Cache flushed successfully. "
