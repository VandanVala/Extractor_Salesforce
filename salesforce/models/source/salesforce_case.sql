SELECT
    Id as id,
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
FROM {{source('Salesforce','case')}}