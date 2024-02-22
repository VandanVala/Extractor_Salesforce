
  create view "Salesforce"."public"."salesforce_user__dbt_tmp"
    
    
  as (
    SELECT 
    "Id" as id,
    "CreatedDate",
    "SystemModstamp",
    "Username",
    "Name",
    "CompanyName",
    "Email",
    "ProfileId",
    "UserType",
    "LastLoginDate",
    "IsActive",
    "UserRoleId",
    "CreatedById",
    "LastModifiedDate",
    "LastModifiedById"
FROM "Salesforce"."public"."user"
  );