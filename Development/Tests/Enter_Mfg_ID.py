# Enter_Mfg_ID

def Enter_Mfg_ID(mfgIdInput, MessageDisplay):
	mfgId = mfgIdInput.get()
	mfgIdInput.delete(0, 'end')
	MessageDisplay.config(anchor = 'w', text = str( mfgId))
	return mfgId
