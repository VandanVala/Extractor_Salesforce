select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    Contact_Id as unique_field,
    count(*) as n_records

from "Salesforce"."public"."salesforce_contact"
where Contact_Id is not null
group by Contact_Id
having count(*) > 1



      
    ) dbt_internal_test