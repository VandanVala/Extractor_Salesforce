
  create view "Salesforce"."public"."salesforce_contact__dbt_tmp"
    
    
  as (
    SELECT
    Contact_Id,
	Account_Id,
	Owner_Id,
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
	Level__c,
	Languages,
	Street
FROM "Salesforce"."public"."contact"
  );