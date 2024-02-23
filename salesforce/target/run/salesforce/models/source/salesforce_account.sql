
  create view "Salesforce"."public"."salesforce_account__dbt_tmp"
    
    
  as (
    SELECT 
    "Id" AS Id,
    "CreatedDate",
    "SystemModstamp",
    "AccountNumber",
    "Phone",
    "Fax",
    "Website",
    "Industry",
    "Name",
    "Type",
    "BillingStreet",
    "BillingCity",
    "AnnualRevenue",
    "NumberOfEmployees",
    "Rating",
    "Ownership",
    "OwnerId",
    "CreatedById",
    "CustomerPriority__c",
    "Active__c",
    "SLA__c",
    "LastModifiedDate",
    "LastModifiedById",
    "ShippingStreet",
    "Sic",
    "TickerSymbol",
    "Description",
    "CleanStatus",
    "NumberofLocations__c",
    "UpsellOpportunity__c",
    "SLASerialNumber__c",
    "SLAExpirationDate__c"
FROM "Salesforce"."public"."account"
  );