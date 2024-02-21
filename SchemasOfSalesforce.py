from sqlalchemy import text

class SchemasOfSalesforce:
    def __init__(self):
        pass
    
    def get_query(self,table_name, maxdate):
        table_name = table_name.lower()
        query = None

        if table_name == "account" :
            query = (f'SELECT Id,CreatedDate,SystemModstamp,AccountNumber,Phone,Fax,Website,Industry,Name,Type,BillingStreet,BillingCity,ParentId,BillingCountry,AnnualRevenue,NumberOfEmployees,Rating,Ownership,OwnerId,CreatedById,CustomerPriority__c,Active__c,SLA__c FROM Account WHERE SystemModstamp >={maxdate}')
        elif table_name == "opportunity" :
            query = (f'SELECT Id,CreatedDate,SystemModstamp,Name,Type,StageName,Amount,LeadSource,OwnerId,CreatedById,AccountId FROM Opportunity WHERE SystemModstamp >={maxdate}')
        elif table_name == "lead" :
            query = (f'SELECT Id,CreatedDate,SystemModstamp,IsDeleted,Name,Title,Country,Company,Salutation,Street,City,State,Phone,Email,LeadSource,Status,Industry,Rating,AnnualRevenue,OwnerId,IsConverted,CreatedById,LastModifiedDate,LastModifiedById FROM Lead WHERE SystemModstamp >={maxdate}')
        elif table_name == "user" :
            query = (f'SELECT Id,CreatedDate,SystemModstamp,Username,Name,CompanyName,Email,ProfileId,UserType,LastLoginDate,IsActive,UserRoleId,CreatedById,LastModifiedDate,LastModifiedById FROM User WHERE SystemModstamp >={maxdate}')
        return query
    
    def get_update_query(self,table_name,row):
        table_name = table_name.lower()
        query = None

        if table_name == "account" :
            update_query = text(f"""
                UPDATE {table_name}
                SET "Id" = '{row['Id']}',
                    "CreatedDate" = '{row['CreatedDate']}',
                    "SystemModstamp" = '{row['SystemModstamp']}',
                    "AccountNumber" = '{row['AccountNumber']}',
                    "Phone" = '{row['Phone']}',
                    "Fax" = '{row['Fax']}',
                    "Website" = '{row['Website']}',
                    "Industry" = '{row['Industry']}',
                    "Name" = '{row['Name']}',
                    "Type" = '{row['Type']}',
                    "BillingStreet" = '{row['BillingStreet']}',
                    "BillingCity" = '{row['BillingCity']}',
                    "ParentId" = '{row['ParentId']}',
                    "BillingCountry" = '{row['BillingCountry']}',
                    "AnnualRevenue" = '{row['AnnualRevenue']}',
                    "NumberOfEmployees" = '{row['NumberOfEmployees']}',
                    "Rating" = '{row['Rating']}',
                    "Ownership" = '{row['Ownership']}',
                    "OwnerId" = '{row['OwnerId']}',
                    "CreatedById" = '{row['CreatedById']}',
                    "CustomerPriority__c" = '{row['CustomerPriority__c']}',
                    "Active__c" = '{row['Active__c']}',
                    "SLA__c" = '{row['SLA__c']}'
                WHERE "Id" = '{row['Id']}';
                """)
            
        elif table_name == "opportunity" :
            update_query = text(f"""
                UPDATE {table_name}
                SET "Id" = '{row['Id']}',
                    "CreatedDate" = '{row['CreatedDate']}',
                    "SystemModstamp" = '{row['SystemModstamp']}',
                    "Name" = '{row['Name']}',
                    "Type" = '{row['Type']}',
                    "StageName" = '{row['StageName']}',
                    "Amount" = '{row['Amount']}',
                    "LeadSource" = '{row['LeadSource']}',
                    "OwnerId" = '{row['OwnerId']}',
                    "CreatedById" = '{row['CreatedById']}',
                    "AccountId" = '{row['AccountId']}'
                WHERE "Id" = '{row['Id']}';
                """)
        elif table_name == "lead" :
            update_query = text(f"""
                UPDATE {table_name}
                SET "Id" = '{row['Id']}',
                    "CreatedDate" = '{row['CreatedDate']}',
                    "SystemModstamp" = '{row['SystemModstamp']}',
                    "IsDeleted" = '{row['IsDeleted']}',
                    "Name" = '{row['Name']}',
                    "Title" = '{row['Title']}',
                    "Country" = '{row['Country']}',
                    "Company" = '{row['Company']}',
                    "Salutation" = '{row['Salutation']}',
                    "Street" = '{row['Street']}',
                    "City" = '{row['City']}',
                    "State" = '{row['State']}',
                    "Phone" = '{row['Phone']}',
                    "Email" = '{row['Email']}',
                    "LeadSource" = '{row['LeadSource']}',
                    "Status" = '{row['Status']}',
                    "Industry" = '{row['Industry']}',
                    "Rating" = '{row['Rating']}',
                    "AnnualRevenue" = '{row['AnnualRevenue']}',
                    "OwnerId" = '{row['OwnerId']}',
                    "IsConverted" = '{row['IsConverted']}',
                    "CreatedById" = '{row['CreatedById']}',
                    "LastModifiedDate" = '{row['LastModifiedDate']}',
                    "LastModifiedById" = '{row['LastModifiedById']}'
                WHERE "Id" = '{row['Id']}';
                """)
        elif table_name == "user" :
            update_query = text(f"""
                UPDATE public.{table_name}
                SET "Id" = '{row['Id']}',
                    "CreatedDate" = '{row['CreatedDate']}',
                    "SystemModstamp" = '{row['SystemModstamp']}',
                    "Username" = '{row['Username']}',
                    "CompanyName" = '{row['CompanyName']}',
                    "Email" = '{row['Email']}',
                    "ProfileId" = '{row['ProfileId']}',
                    "UserType" = '{row['UserType']}',
                    "Name" = '{row['Name']}',
                    "LastLoginDate" = '{row['LastLoginDate']}',
                    "IsActive" = '{row['IsActive']}',
                    "UserRoleId" = '{row['UserRoleId']}',
                    "LastModifiedDate" = '{row['LastModifiedDate']}',
                    "LastModifiedById" = '{row['LastModifiedById']}',
                    "CreatedById" = '{row['CreatedById']}'
                WHERE "Id" = '{row['Id']}';
                """)
        return update_query
    
    
    def get_column_list(self,table_name):
        table_name = table_name.lower()
        columns_list = []

        if table_name == "account" :
            columns_list = ["Id","CreatedDate","SystemModstamp","AccountNumber","Phone","Fax","Website","Industry","Name","Type","BillingStreet","BillingCity","ParentId","BillingCountry","AnnualRevenue","NumberOfEmployees","Rating","Ownership","OwnerId","CreatedById","CustomerPriority__c","Active__c","SLA__c"]
        elif table_name == "opportunity" :
            columns_list = ["Id","CreatedDate","SystemModstamp","Name","Type","StageName","Amount","LeadSource","OwnerId","CreatedById","AccountId"]
        elif table_name == "lead" :
            columns_list = ["Id","CreatedDate","SystemModstamp","IsDeleted","Name","Title","Country","Company","Salutation","Street","City","State","Phone","Email","LeadSource","Status","Industry","Rating","AnnualRevenue","OwnerId","IsConverted","CreatedById","LastModifiedDate","LastModifiedById"]
        elif table_name == "user" :
            columns_list = ["Id","CreatedDate","SystemModstamp","Username","Name","CompanyName","Email","ProfileId","UserType","LastLoginDate","IsActive","UserRoleId","CreatedById","LastModifiedDate","LastModifiedById"]
        return columns_list
    

