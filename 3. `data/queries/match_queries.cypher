// List all donors and recipients
MATCH (d:Donor)-[:CAN_DONATE]->(o:Organ)<-[:NEEDS]-(r:Recipient)
RETURN d.name AS Donor, o.type AS Organ, r.name AS Recipient;

// Find all organs available in City Hospital
MATCH (h:Hospital {name: "City Hospital"})-[:HAS]->(o:Organ)
RETURN h.name, o.type, o.status;
