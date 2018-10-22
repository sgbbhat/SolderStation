# Enter_Mfg_ID

def Last_ScannedMfgID(mfgIdInput, MessageDisplay):
	mfgId = mfgIdInput.get()
	mfgIdInput.delete(0, 'end')
	MessageDisplay.config(anchor = 'w', text = str( mfgId))
	return mfgId
