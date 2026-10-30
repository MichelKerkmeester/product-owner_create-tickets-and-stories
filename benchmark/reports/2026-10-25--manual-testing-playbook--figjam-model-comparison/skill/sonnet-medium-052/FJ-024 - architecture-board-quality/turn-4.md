<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: sync-service, second glance: the API gateway, the Change stream and the Push worker
Left out: file storage, no source states a call to or from it
Finding: the gateway to sync-service edge (`Routes sync requests`) is assumed, because the doc excerpt you relayed names no call between them. The doc itself would settle it.
Finding: the dashed style on the three async edges was read from the overview screenshot, because `get_figjam` returns no line style.
Finding: the reader (Loomlist Engineering) is assumed, because no source names one.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.