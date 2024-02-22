
  create view "Salesforce"."public"."salesforce_campaign__dbt_tmp"
    
    
  as (
    SELECT
    Id as id,
	Name,
	Type,
	Status,
	StartDate,
	EndDate,
	ExpectedRevenue,
	BudgetedCost,
	ActualCost,
	ExpectedResponse,
	NumberSent,
	OwnerId,
	CreatedDate,
	CreatedById,
	LastModifiedDate,
	LastModifiedById,
	SystemModstamp
FROM "Salesforce"."public"."campaign"
  );