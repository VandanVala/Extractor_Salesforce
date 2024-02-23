
    
    

select
    id as unique_field,
    count(*) as n_records

from "Salesforce"."public"."salesforce_campaign"
where id is not null
group by id
having count(*) > 1


