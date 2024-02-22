
  create view "Salesforce"."public"."salesforce_opportunity__dbt_tmp"
    
    
  as (
    SELECT 
    "Id" as id,
    "CreatedDate",
    "SystemModstamp",
    "Name","Type","StageName","Amount","LeadSource","OwnerId","CreatedById","AccountId","LastModifiedDate","LastModifiedById","Probability","ExpectedRevenue","CloseDate","FiscalQuarter","FiscalYear","DeliveryInstallationStatus__c","OrderNumber__c","CurrentGenerators__c","TrackingNumber__c","MainCompetitors__c"
FROM "Salesforce"."public"."opportunity"
  );