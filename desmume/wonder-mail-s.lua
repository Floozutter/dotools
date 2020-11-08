local CODE = [[
????? ??????? ?????
????? ??????? ?????
]]

local CHAR_TO_STYLUS = (function ()
	function s(x, y) return {x=x, y=y, touch=true} end
	return {
		["#"] = s(0, 0),
		["%"] = s(0, 0),
		["&"] = s(0, 0),
		["+"] = s(0, 0),
		["-"] = s(0, 0),
		["0"] = s(0, 0),
		["1"] = s(0, 0),
		["2"] = s(0, 0),
		["3"] = s(0, 0),
		["4"] = s(0, 0),
		["5"] = s(0, 0),
		["6"] = s(0, 0),
		["7"] = s(0, 0),
		["8"] = s(0, 0),
		["9"] = s(0, 0),
		["="] = s(0, 0),
		["@"] = s(0, 0),
		["C"] = s(0, 0),
		["F"] = s(0, 0),
		["H"] = s(0, 0),
		["J"] = s(0, 0),
		["K"] = s(0, 0),
		["M"] = s(0, 0),
		["N"] = s(0, 0),
		["P"] = s(0, 0),
		["Q"] = s(0, 0),
		["R"] = s(0, 0),
		["S"] = s(0, 0),
		["T"] = s(0, 0),
		["W"] = s(0, 0),
		["X"] = s(0, 0),
		["Y"] = s(0, 0)
	}
end)()

function enter_code(code)
	for c in code:gmatch(".") do
		local s = CHAR_TO_STYLUS[c]
		if s ~= nil then
			stylus.set(s)
			emu.frameadvance()
		end
	end
end

enter_code(CODE)
