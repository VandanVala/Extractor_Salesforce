select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select Contact_Id
from "Salesforce"."public"."salesforce_contact"
where Contact_Id is null



      
    ) dbt_internal_test