select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select Case_id
from "Salesforce"."public"."salesforce_case"
where Case_id is null



      
    ) dbt_internal_test