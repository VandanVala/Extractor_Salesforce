select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    Case_id as unique_field,
    count(*) as n_records

from "Salesforce"."public"."salesforce_case"
where Case_id is not null
group by Case_id
having count(*) > 1



      
    ) dbt_internal_test