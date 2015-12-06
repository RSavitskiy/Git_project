SELECT InstrumentCode , r.RatingValue,ra.RatingAgencyName, rt.RatingTypeCode FROM instrument
JOIN instrumentrating AS ir
ON instrument.ReportingContextId = ir.ReportingContextId
JOIN rating AS r
ON ir.ReportingContextId = r.ReportingContextId
JOIN ratingagency AS ra
ON r.ReportingContextId = ra.ReportingContextId
JOIN ratingtype AS rt
ON r.ReportingContextId=rt.ReportingContextId





