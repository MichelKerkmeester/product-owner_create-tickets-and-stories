<figma-url>
Read-back: 6 of 6 entities, 6 of 6 relationships, 12 of 12 attributes, first glance: Booking
Finding: your request has a room reserved by many bookings and a booking holding one `roomId`. `context/roamstay-context.md` says one booking holds up to 8 rooms. If that applies here, the model needs a junction table between Booking and Room, which the board does not draw.
Finding: I could not confirm that file `<draft-file-key>` sits in the Roamstay Product plan. The file is empty apart from this board, and I created no new file.
Finding: the `get_figjam` read returns each connector's ends and cardinality marks but not its label text. I checked the six labels on the screenshot the composing call returned.
HVR self-scan: 1 hard blockers. Fixed: none. Kept with reason: "offers", the relationship verb you asked for, used literally for a property listing rooms and not as a stand-in for "has".