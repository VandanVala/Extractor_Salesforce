
    
    

select
    Case_id as unique_field,
    count(*) as n_records

from "Salesforce"."public"."salesforce_case"
where Case_id is not null
group by Case_id
having count(*) > 1


