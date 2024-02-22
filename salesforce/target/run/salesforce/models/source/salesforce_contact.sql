
  create view "Salesforce"."public"."salesforce_contact__dbt_tmp"
    
    
  as (
    SELECT
    Id as id,
	AccountId,
	OwnerId,
	CreatedById,
	LastModifiedById,
	Name,
	Salutation,
	Phone,
	Fax,
	MobilePhone,
	Email,
	Title,
	Department,
	LeadSource,
	Birthdate,
	Description,
	CreatedDate,
	LastModifiedDate,
	SystemModstamp,
	LastViewedDate,
	LastReferencedDate,
	Level,
	Languages,
	Street
FROM "Salesforce"."public"."contact"
  );