
  create view "Salesforce"."public"."salesforce_old_case__dbt_tmp"
    
    
  as (
    SELECT
    Id AS Id,
	CaseNumber ,
	ContactId ,
	AccountId,
	Type,
	Status,
	Reason,
	Origin,
	Subject,
	Priority,
	ClosedDate,
	OwnerId,
	CreatedDate,
	CreatedById,
	LastModifiedDate,
	LastModifiedById,
	SystemModstamp,
	ContactPhone,
	ContactMobile,
	ContactEmail,
	ContactFax,
	LastViewedDate,
	LastReferencedDate,
	EngineeringReqNumber,
	Product,
	PotentialLiability
FROM "Salesforce"."public"."old_case"
  );