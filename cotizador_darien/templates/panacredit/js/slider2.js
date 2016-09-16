/*----------------------------------------------------------------------------\
|                                Slider2 1.02                                  |
|-----------------------------------------------------------------------------|
|                         Created by Erik Arvidsson                           |
|                  (http://webfx.eae.net/contact.html#erik)                   |
|                      For WebFX (http://webfx.eae.net/)                      |
|-----------------------------------------------------------------------------|
| A  Slider2  control that  degrades  to an  input control  for non  supported |
| browsers.                                                                   |
|-----------------------------------------------------------------------------|
|                Copyright (c) 2002, 2003, 2006 Erik Arvidsson                |
|-----------------------------------------------------------------------------|
| Licensed under the Apache License, Version 2.0 (the "License"); you may not |
| use this file except in compliance with the License.  You may obtain a copy |
| of the License at http://www.apache.org/licenses/LICENSE-2.0                |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
| Unless  required  by  applicable law or  agreed  to  in  writing,  software |
| distributed under the License is distributed on an  "AS IS" BASIS,  WITHOUT |
| WARRANTIES OR  CONDITIONS OF ANY KIND,  either express or implied.  See the |
| License  for the  specific language  governing permissions  and limitations |
| under the License.                                                          |
|-----------------------------------------------------------------------------|
| Dependencies: timer.js - an OO abstraction of timers                        |
|               range.js - provides the data model for the Slider2             |
|               winclassic.css or any other css file describing the look      |
|-----------------------------------------------------------------------------|
| 2002-10-14 | Original version released                                      |
| 2003-03-27 | Added a test in the constructor for missing oElement arg       |
| 2003-11-27 | Only use mousewheel when focused                               |
| 2006-05-28 | Changed license to Apache Software License 2.0.                |
|-----------------------------------------------------------------------------|
| Created 2002-10-14 | All changes are in the log above. | Updated 2006-05-28 |
\----------------------------------------------------------------------------*/

Slider2.isSupported = typeof document.createElement != "undefined" &&
	typeof document.documentElement != "undefined" &&
	typeof document.documentElement.offsetWidth == "number";


function Slider2(oElement, oInput, sOrientation) {
	if (!oElement) return;
	this._orientation = sOrientation || "horizontal";
	this._range = new Range2();
	this._range.setExtent2(0);
	this._blockIncrement = 100;
	this._unitIncrement = 10;
	this._timer = new Timer(100);


	if (Slider2.isSupported && oElement) {

		this.document = oElement.ownerDocument || oElement.document;

		this.element = oElement;
		this.element.Slider2 = this;
		this.element.unselectable = "on";

		// add class name tag to class name
		this.element.className = this._orientation + " " + this.classNameTag + " " + this.element.className;

		// create line
		this.line = this.document.createElement("DIV");
		this.line.className = "line";
		this.line.unselectable = "on";
		this.line.appendChild(this.document.createElement("DIV"));
		this.element.appendChild(this.line);

		// create handle
		this.handle = this.document.createElement("DIV");
		this.handle.className = "handle";
		this.handle.unselectable = "on";
		this.handle.appendChild(this.document.createElement("DIV"));
		this.handle.firstChild.appendChild(
			this.document.createTextNode(String.fromCharCode(160)));
		this.element.appendChild(this.handle);
	}

	this.input = oInput;

	// events
	var oThis = this;
	this._range.onchange = function () {
		oThis.recalculate2();
		if (typeof oThis.onchange == "function")
			oThis.onchange();
	};

	if (Slider2.isSupported && oElement) {
		this.element.onfocus		= Slider2.eventHandlers.onfocus;
		this.element.onblur			= Slider2.eventHandlers.onblur;
		this.element.onmousedown	= Slider2.eventHandlers.onmousedown;
		this.element.onmouseover	= Slider2.eventHandlers.onmouseover;
		this.element.onmouseout		= Slider2.eventHandlers.onmouseout;
		this.element.onkeydown		= Slider2.eventHandlers.onkeydown;
		this.element.onkeypress		= Slider2.eventHandlers.onkeypress;
		this.element.onmousewheel	= Slider2.eventHandlers.onmousewheel;
		this.handle.onselectstart	=
		this.element.onselectstart	= function () { return false; };

		this._timer.ontimer2 = function () {
			oThis.ontimer2();
		};

		// extra recalculate for ie
		window.setTimeout(function() {
			oThis.recalculate2();
		}, 1);
	}
	else {
		this.input.onchange = function (e) {
			othis.setValue22(oThis.input.value);
		};
	}
}

Slider2.eventHandlers = {

	// helpers to make events a bit easier
	getEvent:	function (e, el) {
		if (!e) {
			if (el)
				e = el.document.parentWindow.event;
			else
				e = window.event;
		}
		if (!e.srcElement) {
			var el = e.target;
			while (el != null && el.nodeType != 1)
				el = el.parentNode;
			e.srcElement = el;
		}
		if (typeof e.offsetX == "undefined") {
			e.offsetX = e.layerX;
			e.offsetY = e.layerY;
		}

		return e;
	},

	getDocument:	function (e) {
		if (e.target)
			return e.target.ownerDocument;
		return e.srcElement.document;
	},

	getSlider:	function (e) {
		var el = e.target || e.srcElement;
		while (el != null && el.Slider2 == null)	{
			el = el.parentNode;
		}
		if (el)
			return el.Slider2;
		return null;
	},

	getLine:	function (e) {
		var el = e.target || e.srcElement;
		while (el != null && el.className != "line")	{
			el = el.parentNode;
		}
		return el;
	},

	getHandle:	function (e) {
		var el = e.target || e.srcElement;
		var re = /handle/;
		while (el != null && !re.test(el.className))	{
			el = el.parentNode;
		}
		return el;
	},
	// end helpers

	onfocus:	function (e) {
		var s = this.Slider2;
		s._focused = true;
		s.handle.className = "handle hover";
	},

	onblur:	function (e) {
		var s = this.Slider2
		s._focused = false;
		s.handle.className = "handle";
	},

	onmouseover:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);
		var s = this.Slider2;
		if (e.srcElement == s.handle)
			s.handle.className = "handle hover";
	},

	onmouseout:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);
		var s = this.Slider2;
		if (e.srcElement == s.handle && !s._focused)
			s.handle.className = "handle";
	},

	onmousedown:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);
		var s = this.Slider2;
		if (s.element.focus)
			s.element.focus();

		Slider2._currentInstance = s;
		var doc = s.document;

		if (doc.addEventListener) {
			doc.addEventListener("mousemove", Slider2.eventHandlers.onmousemove, true);
			doc.addEventListener("mouseup", Slider2.eventHandlers.onmouseup, true);
		}
		else if (doc.attachEvent) {
			doc.attachEvent("onmousemove", Slider2.eventHandlers.onmousemove);
			doc.attachEvent("onmouseup", Slider2.eventHandlers.onmouseup);
			doc.attachEvent("onlosecapture", Slider2.eventHandlers.onmouseup);
			s.element.setCapture();
		}

		if (Slider2.eventHandlers.getHandle(e)) {	// start drag
			Slider2._SliderDragData = {
				screenX:	e.screenX,
				screenY:	e.screenY,
				dx:			e.screenX - s.handle.offsetLeft,
				dy:			e.screenY - s.handle.offsetTop,
				startValue:	s.getValue2(),
				Slider2:		s
			};
		}
		else {
			var lineEl = Slider2.eventHandlers.getLine(e);
			s._mouseX = e.offsetX + (lineEl ? s.line.offsetLeft : 0);
			s._mouseY = e.offsetY + (lineEl ? s.line.offsetTop : 0);
			s._increasing = null;
			s.ontimer2();
		}
	},

	onmousemove:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);

		if (Slider2._SliderDragData) {	// drag
			var s = Slider2._SliderDragData.Slider2;

			var boundSize = s.getMaximum2() - s.getMinimum2();
			var size, pos, reset;

			if (s._orientation == "horizontal") {
				size = s.element.offsetWidth - s.handle.offsetWidth;
				pos = e.screenX - Slider2._SliderDragData.dx;
				reset = Math.abs(e.screenY - Slider2._SliderDragData.screenY) > 100;
			}
			else {
				size = s.element.offsetHeight - s.handle.offsetHeight;
				pos = s.element.offsetHeight - s.handle.offsetHeight -
					(e.screenY - Slider2._SliderDragData.dy);
				reset = Math.abs(e.screenX - Slider2._SliderDragData.screenX) > 100;
			}
			s.setValue2(reset ? Slider2._SliderDragData.startValue :
						s.getMinimum2() + boundSize * pos / size);
			return false;
		}
		else {
			var s = Slider2._currentInstance;
			if (s != null) {
				var lineEl = Slider2.eventHandlers.getLine(e);
				s._mouseX = e.offsetX + (lineEl ? s.line.offsetLeft : 0);
				s._mouseY = e.offsetY + (lineEl ? s.line.offsetTop : 0);
			}
		}

	},

	onmouseup:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);
		var s = Slider2._currentInstance;
		var doc = s.document;
		if (doc.removeEventListener) {
			doc.removeEventListener("mousemove", Slider2.eventHandlers.onmousemove, true);
			doc.removeEventListener("mouseup", Slider2.eventHandlers.onmouseup, true);
		}
		else if (doc.detachEvent) {
			doc.detachEvent("onmousemove", Slider2.eventHandlers.onmousemove);
			doc.detachEvent("onmouseup", Slider2.eventHandlers.onmouseup);
			doc.detachEvent("onlosecapture", Slider2.eventHandlers.onmouseup);
			s.element.releaseCapture();
		}

		if (Slider2._SliderDragData) {	// end drag
			Slider2._SliderDragData = null;
		}
		else {
			s._timer.stop();
			s._increasing = null;
		}
		Slider2._currentInstance = null;
	},

	onkeydown:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);
		//var s = Slider2.eventHandlers.getSlider2(e);
		var s = this.Slider2;
		var kc = e.keyCode;
		switch (kc) {
			case 33:	// page up
				s.setValue2(s.getValue2() + s.getBlockIncrement());
				break;
			case 34:	// page down
				s.setValue2(s.getValue2() - s.getBlockIncrement());
				break;
			case 35:	// end
				s.setValue2(s.getOrientation() == "horizontal" ?
					s.getMaximum2() :
					s.getMinimum2());
				break;
			case 36:	// home
				s.setValue2(s.getOrientation() == "horizontal" ?
					s.getMinimum2() :
					s.getMaximum2());
				break;
			case 38:	// up
			case 39:	// right
				s.setValue2(s.getValue2() + s.getUnitIncrement());
				break;

			case 37:	// left
			case 40:	// down
				s.setValue2(s.getValue2() - s.getUnitIncrement());
				break;
		}

		if (kc >= 33 && kc <= 40) {
			return false;
		}
	},

	onkeypress:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);
		var kc = e.keyCode;
		if (kc >= 33 && kc <= 40) {
			return false;
		}
	},

	onmousewheel:	function (e) {
		e = Slider2.eventHandlers.getEvent(e, this);
		var s = this.Slider2;
		if (s._focused) {
			s.setValue2(s.getValue2() + e.wheelDelta / 120 * s.getUnitIncrement()); // AQUIII PARA CAMBIAR EL STEP
			// windows inverts this on horizontal Slider2s. That does not
			// make sense to me
			return false;
		}
	}
};



Slider2.prototype.classNameTag = "dynamic-slider-control",

Slider2.prototype.setValue2 = function (v) {
	this._range.setValue2(v);
	this.input.value = this.getValue2();
};

Slider2.prototype.getValue2 = function () {
	return this._range.getValue2();
};

Slider2.prototype.setMinimum2 = function (v) {
	this._range.setMinimum2(v);
	this.input.value = this.getValue2();
};

Slider2.prototype.getMinimum2 = function () {
	return this._range.getMinimum2();
};

Slider2.prototype.setMaximum2 = function (v) {
	this._range.setMaximum2(v);
	this.input.value = this.getValue2();
};

Slider2.prototype.getMaximum2 = function () {
	return this._range.getMaximum2();
};

Slider2.prototype.setUnitIncrement = function (v) {
	this._unitIncrement = v;
};

Slider2.prototype.getUnitIncrement = function () {
	return this._unitIncrement;
};

Slider2.prototype.setBlockIncrement = function (v) {
	this._blockIncrement = v;
};

Slider2.prototype.getBlockIncrement = function () {
	return this._blockIncrement;
};

Slider2.prototype.getOrientation = function () {
	return this._orientation;
};

Slider2.prototype.setOrientation = function (sOrientation) {
	if (sOrientation != this._orientation) {
		if (Slider2.isSupported && this.element) {
			// add class name tag to class name
			this.element.className = this.element.className.replace(this._orientation,
									sOrientation);
		}
		this._orientation = sOrientation;
		this.recalculate2();

	}
};

Slider2.prototype.recalculate2 = function() {
	if (!Slider2.isSupported || !this.element) return;

	var w = this.element.offsetWidth;
	var h = this.element.offsetHeight;
	var hw = this.handle.offsetWidth;
	var hh = this.handle.offsetHeight;
	var lw = this.line.offsetWidth;
	var lh = this.line.offsetHeight;

	// this assumes a border-box layout

	if (this._orientation == "horizontal") {
		this.handle.style.left = (w - hw) * (this.getValue2() - this.getMinimum2()) /
			(this.getMaximum2() - this.getMinimum2()) + "px";
		this.handle.style.top = (h - hh) / 2 + "px";

		this.line.style.top = (h - lh) / 2 + "px";
		this.line.style.left = hw / 2 + "px";
		//this.line.style.right = hw / 2 + "px";
		this.line.style.width = Math.max(0, w - hw - 2)+ "px";
		this.line.firstChild.style.width = Math.max(0, w - hw - 4)+ "px";
	}
	else {
		this.handle.style.left = (w - hw) / 2 + "px";
		this.handle.style.top = h - hh - (h - hh) * (this.getValue2() - this.getMinimum2()) /
			(this.getMaximum2() - this.getMinimum2()) + "px";

		this.line.style.left = (w - lw) / 2 + "px";
		this.line.style.top = hh / 2 + "px";
		this.line.style.height = Math.max(0, h - hh - 2) + "px";	//hard coded border width
		//this.line.style.bottom = hh / 2 + "px";
		this.line.firstChild.style.height = Math.max(0, h - hh - 4) + "px";	//hard coded border width
	}
};

Slider2.prototype.ontimer2 = function () {
	var hw = this.handle.offsetWidth;
	var hh = this.handle.offsetHeight;
	var hl = this.handle.offsetLeft;
	var ht = this.handle.offsetTop;

	if (this._orientation == "horizontal") {
		if (this._mouseX > hl + hw &&
			(this._increasing == null || this._increasing)) {
			this.setValue22(this.getValue2() + this.getBlockIncrement());
			this._increasing = true;
		}
		else if (this._mouseX < hl &&
			(this._increasing == null || !this._increasing)) {
			this.setValue22(this.getValue2() - this.getBlockIncrement());
			this._increasing = false;
		}
	}
	else {
		if (this._mouseY > ht + hh &&
			(this._increasing == null || !this._increasing)) {
			this.setValue22(this.getValue2() - this.getBlockIncrement());
			this._increasing = false;
		}
		else if (this._mouseY < ht &&
			(this._increasing == null || this._increasing)) {
			this.setValue22(this.getValue2() + this.getBlockIncrement());
			this._increasing = true;
		}
	}

	this._timer.start();
};