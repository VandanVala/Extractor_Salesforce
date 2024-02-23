
    
    

select
    id as unique_field,
    count(*) as n_records

from "Salesforce"."public"."salesforce_old_contact"
where id is not null
group by id
having count(*) > 1


