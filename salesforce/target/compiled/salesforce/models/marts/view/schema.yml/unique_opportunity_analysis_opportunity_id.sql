
    
    

select
    opportunity_id as unique_field,
    count(*) as n_records

from "Salesforce"."public"."opportunity_analysis"
where opportunity_id is not null
group by opportunity_id
having count(*) > 1


