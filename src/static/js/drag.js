function toggleDisplay(divId) {
  var x = document.getElementById(divId);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

      var width = window.innerWidth;
      var height = window.innerHeight;

      var stage = new Konva.Stage({
        container: 'konva-container',
        width: (10*width)/12,
        height: height
      });

      var layer = new Konva.Layer();
      var rectX = stage.width() / 2 - 50;
      var rectY = stage.height() / 2 - 25;


      var box = new Konva.Rect({
        x: rectX,
        y: rectY,
        width: 10,
        height: 10,
        fill: '#00D2FF',
        stroke: 'black',
        strokeWidth: 2,
        draggable: true
      });

      var box1 = new Konva.Rect({
        x: rectX + 20,
        y: rectY,
        width: 10,
        height: 10,
        fill: '#00D2FF',
        stroke: 'black',
        strokeWidth: 2,
        draggable: true
      });

      var box2 = new Konva.Rect({
        x: rectX + 20,
        y: rectY + 20,
        width: 10,
        height: 10,
        fill: '#00D2FF',
        stroke: 'black',
        strokeWidth: 2,
        draggable: true
      });

      var box3 = new Konva.Rect({
        x: rectX,
        y: rectY + 20,
        width: 10,
        height: 10,
        fill: '#00D2FF',
        stroke: 'black',
        strokeWidth: 2,
        draggable: true
      });
      
      var line = new Konva.Line({
        points: [box.getX()+5, box.getY()+5, box1.getX()+5, box1.getY()+5, box2.getX()+5, box2.getY()+5, box3.getX()+5, box3.getY()+5, box.getX()+5, box.getY()+5],
        stroke: 'red',
        strokeWidth: 3
      });

      box.moveToTop();
      box1.moveToTop();
      box2.moveToTop();
      box3.moveToTop();
      layer.draw();
      
      box.on('dragmove', function() {
        line.setPoints([box.getX()+5, box.getY()+5, box1.getX()+5, box1.getY()+5, box2.getX()+5, box2.getY()+5, box3.getX()+5, box3.getY()+5, box.getX()+5, box.getY()+5]);
        var st = document.getElementById('zoomed-image').style.backgroundPosition.split(" ");
        var lt = Number(st[0].replace(/px$/, ''));
        var ut = Number(st[1].replace(/px$/, ''));
        var obj = document.getElementById('plus');
        var xpos = obj.offsetTop + obj.offsetHeight/4 - lt;
        var ypos = obj.offsetTop + obj.offsetHeight/2 - ut;
        var width = Number(4*document.getElementById('image').width);
        var mul = 3840/width;
        xpos *= mul;
        ypos *= mul;
        // ypos += 2.5;
        document.getElementById("point1").value = Math.round(xpos) + " " + Math.round(ypos);
      });
      box1.on('dragmove', function() {
        line.setPoints([box.getX()+5, box.getY()+5, box1.getX()+5, box1.getY()+5, box2.getX()+5, box2.getY()+5, box3.getX()+5, box3.getY()+5, box.getX()+5, box.getY()+5]);
        var st = document.getElementById('zoomed-image').style.backgroundPosition.split(" ");
        var lt = Number(st[0].replace(/px$/, ''));
        var ut = Number(st[1].replace(/px$/, ''));
        var obj = document.getElementById('plus');
        var xpos = obj.offsetTop + obj.offsetHeight/4 - lt;
        var ypos = obj.offsetTop + obj.offsetHeight/2 - ut;
        var width = Number(4*document.getElementById('image').width);
        var mul = 3840/width;
        xpos *= mul;
        ypos *= mul;
        // ypos += 2.5;
        document.getElementById("point2").value = Math.round(xpos) + " " + Math.round(ypos);
      });
      box2.on('dragmove', function() {
        line.setPoints([box.getX()+5, box.getY()+5, box1.getX()+5, box1.getY()+5, box2.getX()+5, box2.getY()+5, box3.getX()+5, box3.getY()+5, box.getX()+5, box.getY()+5]);
        var st = document.getElementById('zoomed-image').style.backgroundPosition.split(" ");
        var lt = Number(st[0].replace(/px$/, ''));
        var ut = Number(st[1].replace(/px$/, ''));
        var obj = document.getElementById('plus');
        var xpos = obj.offsetTop + obj.offsetHeight/4 - lt;
        var ypos = obj.offsetTop + obj.offsetHeight/2 - ut;
        var width = Number(4*document.getElementById('image').width);
        var mul = 3840/width;
        xpos *= mul;
        ypos *= mul;
        // ypos += 2.5;
        document.getElementById("point3").value = Math.round(xpos) + " " + Math.round(ypos);
      });
      box3.on('dragmove', function() {
        line.setPoints([box.getX()+5, box.getY()+5, box1.getX()+5, box1.getY()+5, box2.getX()+5, box2.getY()+5, box3.getX()+5, box3.getY()+5, box.getX()+5, box.getY()+5]);
        var st = document.getElementById('zoomed-image').style.backgroundPosition.split(" ");
        var lt = Number(st[0].replace(/px$/, ''));
        var ut = Number(st[1].replace(/px$/, ''));
        var obj = document.getElementById('plus');
        var xpos = obj.offsetTop + obj.offsetHeight/4 - lt;
        var ypos = obj.offsetTop + obj.offsetHeight/2 - ut;
        var width = Number(4*document.getElementById('image').width);
        var mul = 3840/width;
        xpos *= mul;
        ypos *= mul;
        // ypos += 2.5;
        document.getElementById("point4").value = Math.round(xpos) + " " + Math.round(ypos);
      });

      box.on('dragstart', function () {
        toggleDisplay("output-img");
        toggleDisplay("top-left");
      });

      box.on('dragend', function () {
        toggleDisplay("output-img");
        toggleDisplay("top-left");
      });

      box1.on('dragstart', function () {
        toggleDisplay("output-img");
        toggleDisplay("top-right");
      });

      box1.on('dragend', function () {
        toggleDisplay("output-img");
        toggleDisplay("top-right");
      });

      box2.on('dragstart', function () {
        toggleDisplay("output-img");
        toggleDisplay("bottom-right");
      });

      box2.on('dragend', function () {
        toggleDisplay("output-img");
        toggleDisplay("bottom-right");
      });

      box3.on('dragstart', function () {
        toggleDisplay("output-img");
        toggleDisplay("bottom-left");
      });

      box3.on('dragend', function () {
        toggleDisplay("output-img");
        toggleDisplay("bottom-left");
      });

      layer.add(line);
      layer.add(box);
      layer.add(box1);
      layer.add(box2);
      layer.add(box3);
      layer.batchDraw();

      stage.add(layer);