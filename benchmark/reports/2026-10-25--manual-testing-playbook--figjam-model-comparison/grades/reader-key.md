# Reader key

Each reader saw one board of every scenario. Reader n saw model (n - 1 + scenario index) mod 3,
with the scenarios in the order FJ-022 to FJ-028 and the models in the order deepseek, glm, swe.

## FJ-022, reader 1: deepseek (108-4364)

- Q1: What does a customer see more than 30 days after delivery? Answer: Contact support
- Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup
- Q3: Is the free pickup over 100 euros live? Answer: it is not on the board, and the reply names it under Left out

## FJ-023, reader 1: glm (112-4566)

- Q1: Who books the courier pickup? Answer: the warehouse operator
- Q2: What happens when the damage is unclear? Answer: the customer sends a second photo and CS checks again
- Q3: Where does the claim change teams? Answer: from CS approving the claim to the warehouse booking the pickup

## FJ-024, reader 1: swe (117-4812)

- Q1: Which part do the clients connect to? Answer: the API gateway
- Q2: How does a sleeping iOS device find out about a change? Answer: sync-service publishes to the change stream, the push worker reads it and calls Apple Push
- Q3: Which connections do not wait for an answer? Answer: the three dotted ones: publishes, consumes and the Apple Push call

## FJ-025, reader 1: deepseek (121-4040)

- Q1: Who authorises the card? Answer: the payment provider
- Q2: Which message does not wait for a reply? Answer: BookingCreated to the partner hub
- Q3: What does the app get back? Answer: 201 Booking confirmed

## FJ-026, reader 1: glm (126-4597)

- Q1: Which states end a booking? Answer: Completed, Cancelled and No-show
- Q2: From which states can a guest cancel? Answer: Pending and Confirmed
- Q3: What moves a booking from Upcoming to In stay? Answer: check in

## FJ-027, reader 1: swe (132-5151)

- Q1: How many rooms does one booking reserve? Answer: one
- Q2: Which entity publishes rate plans? Answer: Property
- Q3: Can one booking hold several payments? Answer: yes

## FJ-028, reader 1: deepseek (141-5330)

- Q1: Which task is on the critical path? Answer: Integration
- Q2: What must finish before integration starts? Answer: the sync engine and the conflict screen build
- Q3: When is the release? Answer: 21 December 2026, after the beta

## FJ-022, reader 2: glm (109-4426)

- Q1: What does a customer see more than 30 days after delivery? Answer: Contact support
- Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup
- Q3: Is the free pickup over 100 euros live? Answer: it is not on the board, and the reply names it under Left out

## FJ-023, reader 2: swe (114-4602)

- Q1: Who books the courier pickup? Answer: the warehouse operator
- Q2: What happens when the damage is unclear? Answer: the customer sends a second photo and CS checks again
- Q3: Where does the claim change teams? Answer: from CS approving the claim to the warehouse booking the pickup

## FJ-024, reader 2: deepseek (118-4935)

- Q1: Which part do the clients connect to? Answer: the API gateway
- Q2: How does a sleeping iOS device find out about a change? Answer: sync-service publishes to the change stream, the push worker reads it and calls Apple Push
- Q3: Which connections do not wait for an answer? Answer: the three dotted ones: publishes, consumes and the Apple Push call

## FJ-025, reader 2: glm (122-4181)

- Q1: Who authorises the card? Answer: the payment provider
- Q2: Which message does not wait for a reply? Answer: BookingCreated to the partner hub
- Q3: What does the app get back? Answer: 201 Booking confirmed

## FJ-026, reader 2: swe (129-4747)

- Q1: Which states end a booking? Answer: Completed, Cancelled and No-show
- Q2: From which states can a guest cancel? Answer: Pending and Confirmed
- Q3: What moves a booking from Upcoming to In stay? Answer: check in

## FJ-027, reader 2: deepseek (134-5211)

- Q1: How many rooms does one booking reserve? Answer: one
- Q2: Which entity publishes rate plans? Answer: Property
- Q3: Can one booking hold several payments? Answer: yes

## FJ-028, reader 2: glm (145-5350)

- Q1: Which task is on the critical path? Answer: Integration
- Q2: What must finish before integration starts? Answer: the sync engine and the conflict screen build
- Q3: When is the release? Answer: 21 December 2026, after the beta

## FJ-022, reader 3: swe (111-4498)

- Q1: What does a customer see more than 30 days after delivery? Answer: Contact support
- Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup
- Q3: Is the free pickup over 100 euros live? Answer: it is not on the board, and the reply names it under Left out

## FJ-023, reader 3: deepseek (116-4717)

- Q1: Who books the courier pickup? Answer: the warehouse operator
- Q2: What happens when the damage is unclear? Answer: the customer sends a second photo and CS checks again
- Q3: Where does the claim change teams? Answer: from CS approving the claim to the warehouse booking the pickup

## FJ-024, reader 3: glm (119-5058)

- Q1: Which part do the clients connect to? Answer: the API gateway
- Q2: How does a sleeping iOS device find out about a change? Answer: sync-service publishes to the change stream, the push worker reads it and calls Apple Push
- Q3: Which connections do not wait for an answer? Answer: the three dotted ones: publishes, consumes and the Apple Push call

## FJ-025, reader 3: swe (123-4329, 124-4477)

- Q1: Who authorises the card? Answer: the payment provider
- Q2: Which message does not wait for a reply? Answer: BookingCreated to the partner hub
- Q3: What does the app get back? Answer: 201 Booking confirmed

## FJ-026, reader 3: deepseek (131-5009)

- Q1: Which states end a booking? Answer: Completed, Cancelled and No-show
- Q2: From which states can a guest cancel? Answer: Pending and Confirmed
- Q3: What moves a booking from Upcoming to In stay? Answer: check in

## FJ-027, reader 3: glm (138-5271)

- Q1: How many rooms does one booking reserve? Answer: one
- Q2: Which entity publishes rate plans? Answer: Property
- Q3: Can one booking hold several payments? Answer: yes

## FJ-028, reader 3: swe (146-5370)

- Q1: Which task is on the critical path? Answer: Integration
- Q2: What must finish before integration starts? Answer: the sync engine and the conflict screen build
- Q3: When is the release? Answer: 21 December 2026, after the beta
