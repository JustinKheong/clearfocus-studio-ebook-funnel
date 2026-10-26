from pathlib import Path
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "downloads"
COPY = ROOT / "output" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)
COPY.mkdir(parents=True, exist_ok=True)

INK = HexColor("#082f26")
ORANGE = HexColor("#ef5b22")
CREAM = HexColor("#f7f2e9")
MIST = HexColor("#dfe8dc")
PALE = HexColor("#fffaf4")
GREY = HexColor("#53625d")

def header(c, title, kicker, page, total, landscape_page=False):
    w, h = landscape(A4) if landscape_page else A4
    c.setFillColor(CREAM); c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(ORANGE); c.rect(16*mm, h-17*mm, 7*mm, 7*mm, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 10); c.drawString(26*mm, h-13*mm, "CLEARFOCUS STUDIO")
    c.setFillColor(ORANGE); c.setFont("Helvetica-Bold", 8); c.drawString(16*mm, h-31*mm, kicker.upper())
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 25); c.drawString(16*mm, h-43*mm, title)
    c.setFillColor(GREY); c.setFont("Helvetica", 8); c.drawRightString(w-16*mm, 11*mm, f"{page} / {total}")
    return w, h

def para(c, text, x, y, width, size=10, leading=14, color=GREY, bold=False):
    style = ParagraphStyle("p", fontName="Helvetica-Bold" if bold else "Helvetica", fontSize=size, leading=leading, textColor=color)
    p = Paragraph(text, style); _, ph = p.wrap(width, 200*mm); p.drawOn(c, x, y-ph); return y-ph

def reset_pdf(path):
    c = canvas.Canvas(str(path), pagesize=A4)
    w,h=A4
    c.setFillColor(INK); c.rect(0,0,w,h,fill=1,stroke=0)
    c.setFillColor(ORANGE); c.setLineWidth(1)
    for off in range(-40, 160, 18):
        c.arc(w-78*mm+off, h-85*mm+off/2, w+45*mm+off, h+35*mm+off/2, 205, 95)
    c.setFillColor(white); c.setFont("Helvetica-Bold",34); c.drawString(22*mm,h-75*mm,"THE")
    c.drawString(22*mm,h-91*mm,"FOCUS")
    c.drawString(22*mm,h-107*mm,"RESET")
    c.setFont("Helvetica",11); c.drawString(22*mm,h-123*mm,"A practical guide for a clearer workday")
    c.setFont("Helvetica-Bold",10); c.drawString(22*mm,20*mm,"CLEARFOCUS STUDIO")
    c.showPage()

    pages = [
      ("Start with what matters", "A clear day begins with a small number of meaningful outcomes.", [
       ("1. Empty your head", "List every open task, request, worry and reminder. Capture first; organise second."),
       ("2. Choose one meaningful outcome", "Ask: if only one thing moved forward today, which result would matter most?"),
       ("3. Name the next visible action", "Turn the outcome into an action you can start in under five minutes."),
       ("4. Define done", "Write a simple finish line so you know when to stop polishing.")]),
      ("Use the Focus Filter", "Sort work by impact and urgency before your inbox chooses for you.", [
       ("Do now", "High impact and genuinely time-sensitive. Protect a specific block for it."),
       ("Schedule", "High impact, not urgent. Put it on the calendar before it becomes urgent."),
       ("Delegate", "Necessary work that another person can complete with clear context."),
       ("Remove", "Low-value work that does not support a current priority.")]),
      ("Reduce the pull of distractions", "You do not need more willpower; you need fewer invitations to switch.", [
       ("Silence the obvious", "Pause non-essential notifications and close tabs unrelated to the current task."),
       ("Create a capture lane", "Keep one small note nearby for thoughts that appear while you focus."),
       ("Set response windows", "Choose two or three times to check messages instead of reacting all day."),
       ("Make starting easy", "Prepare the file, reference and first action before the focus block begins.")]),
      ("Work in protected blocks", "A repeatable focus block is short enough to start and long enough to matter.", [
       ("Plan 45-75 minutes", "Choose a duration that fits your energy and the task's complexity."),
       ("State the target", "Write the single result you want from the block."),
       ("Use a gentle timer", "Let time create a boundary, not pressure. Stop briefly when it ends."),
       ("Record the next step", "Before leaving, write exactly where to resume.")]),
      ("Reset when attention slips", "Losing focus is information, not failure.", [
       ("Notice", "Name what pulled you away: a thought, message, unclear task or low energy."),
       ("Park", "Write the distraction in your capture lane so your brain can release it."),
       ("Shrink", "Reduce the next action until it feels unambiguous and light enough to begin."),
       ("Restart", "Return for ten minutes. Momentum often follows movement.")]),
      ("Build a calmer routine", "A useful routine supports real life instead of demanding perfect days.", [
       ("Morning", "Choose the day's priority before opening reactive channels."),
       ("Midday", "Check progress, reset your workspace and adjust the plan."),
       ("Shutdown", "Capture loose ends, choose tomorrow's first action and close the day."),
       ("Weekly", "Review what moved, what distracted you and what to change next week.")]),
    ]
    total=8
    for idx,(title,sub,items) in enumerate(pages,2):
        w,h=header(c,title,"The Focus Reset",idx,total)
        y=h-55*mm; y=para(c,sub,16*mm,y,w-32*mm,11,16,INK)
        y-=8*mm
        for n,(head,body) in enumerate(items,1):
            c.setFillColor(ORANGE); c.circle(22*mm,y-3*mm,5*mm,fill=1,stroke=0)
            c.setFillColor(white); c.setFont("Helvetica-Bold",9); c.drawCentredString(22*mm,y-4.5*mm,str(n))
            c.setFillColor(INK); c.setFont("Helvetica-Bold",12); c.drawString(32*mm,y,head)
            y=para(c,body,32*mm,y-4*mm,w-50*mm,10,14,GREY)-8*mm
        c.showPage()

    w,h=header(c,"Your 10-minute reset","The Focus Reset",8,8)
    y=h-58*mm
    prompts=["The one outcome that matters today is...","The smallest next action is...","I will protect this time block...","The distraction I can remove now is...","When I finish, I will record..."]
    for p in prompts:
        c.setFillColor(INK); c.setFont("Helvetica-Bold",11); c.drawString(18*mm,y,p)
        c.setStrokeColor(HexColor("#b9c6bd"));
        for i in range(3): c.line(18*mm,y-(9+i*9)*mm,w-18*mm,y-(9+i*9)*mm)
        y-=39*mm
    c.save()

def planner_pdf(path):
    c=canvas.Canvas(str(path),pagesize=landscape(A4)); w,h=landscape(A4); total=6
    c.setFillColor(INK); c.rect(0,0,w,h,fill=1,stroke=0)
    c.setStrokeColor(ORANGE); c.setLineWidth(1)
    for off in range(-60,200,20): c.arc(w-100*mm+off, h-80*mm+off/2, w+55*mm+off, h+55*mm+off/2, 205,95)
    c.setFillColor(white); c.setFont("Helvetica-Bold",34); c.drawString(24*mm,h-60*mm,"THE FOCUS PLANNER")
    c.setFont("Helvetica",12); c.drawString(24*mm,h-76*mm,"Printable pages for focused work and calmer weeks")
    c.setFont("Helvetica-Bold",10); c.drawString(24*mm,18*mm,"CLEARFOCUS STUDIO")
    c.showPage()

    w,h=header(c,"Daily Focus Plan","Printable planner",2,total,True)
    c.setFillColor(INK); c.setFont("Helvetica-Bold",11); c.drawString(16*mm,h-57*mm,"DATE")
    c.setStrokeColor(HexColor("#aab9ae")); c.line(34*mm,h-58*mm,90*mm,h-58*mm)
    c.setFillColor(MIST); c.roundRect(16*mm,h-111*mm,105*mm,40*mm,4*mm,fill=1,stroke=0)
    c.setFillColor(INK); c.setFont("Helvetica-Bold",13); c.drawString(23*mm,h-82*mm,"TODAY'S ONE MEANINGFUL OUTCOME")
    c.setStrokeColor(HexColor("#9caf9f"));
    for i in range(2): c.line(23*mm,h-(94+i*10)*mm,113*mm,h-(94+i*10)*mm)
    c.setFont("Helvetica-Bold",12); c.drawString(135*mm,h-74*mm,"TOP THREE NEXT ACTIONS")
    for i in range(3):
        y=h-(87+i*18)*mm; c.setStrokeColor(ORANGE); c.rect(136*mm,y-5*mm,5*mm,5*mm,fill=0,stroke=1); c.setStrokeColor(HexColor("#b9c6bd")); c.line(146*mm,y-3*mm,w-17*mm,y-3*mm)
    c.setFont("Helvetica-Bold",12); c.setFillColor(INK); c.drawString(16*mm,h-132*mm,"FOCUS BLOCKS")
    data=[["TIME","TARGET","DONE"],["","",""],["","",""],["","",""]]
    t=Table(data,colWidths=[28*mm,112*mm,22*mm],rowHeights=[9*mm,15*mm,15*mm,15*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('TEXTCOLOR',(0,0),(-1,0),white),('GRID',(0,0),(-1,-1),.7,HexColor('#9caf9f')),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),4*mm)]));t.wrapOn(c,w,h);t.drawOn(c,16*mm,18*mm)
    c.setFillColor(PALE); c.roundRect(188*mm,18*mm,92*mm,55*mm,4*mm,fill=1,stroke=0); c.setFillColor(INK); c.setFont("Helvetica-Bold",12); c.drawString(195*mm,62*mm,"END-OF-DAY RESET"); para(c,"What moved forward?",195*mm,54*mm,75*mm,9,12,INK,True); para(c,"What is the first step tomorrow?",195*mm,36*mm,75*mm,9,12,INK,True)
    c.showPage()

    w,h=header(c,"Weekly Overview","Printable planner",3,total,True)
    c.setFillColor(INK); c.setFont("Helvetica-Bold",12); c.drawString(16*mm,h-57*mm,"THIS WEEK'S THEME")
    c.setStrokeColor(HexColor("#aab9ae")); c.line(58*mm,h-58*mm,w-16*mm,h-58*mm)
    days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]
    x=16*mm; boxw=(w-40*mm)/5
    for d in days:
        c.setFillColor(PALE); c.roundRect(x,h-155*mm,boxw,78*mm,3*mm,fill=1,stroke=0); c.setFillColor(ORANGE); c.setFont("Helvetica-Bold",9); c.drawString(x+5*mm,h-88*mm,d)
        c.setStrokeColor(HexColor("#c2ccc4"));
        for j in range(5): c.line(x+5*mm,h-(101+j*10)*mm,x+boxw-5*mm,h-(101+j*10)*mm)
        x+=boxw+2*mm
    c.setFillColor(MIST); c.roundRect(16*mm,16*mm,w-32*mm,34*mm,4*mm,fill=1,stroke=0); c.setFillColor(INK); c.setFont("Helvetica-Bold",11); c.drawString(22*mm,41*mm,"PROTECT THESE FOCUS BLOCKS"); c.drawString(155*mm,41*mm,"MAKE THE WEEK LIGHTER BY")
    c.showPage()

    w,h=header(c,"Distraction Log","Printable planner",4,total,True)
    intro="Use this as neutral data. Notice what pulls your attention, then design one small change."
    para(c,intro,16*mm,h-57*mm,w-32*mm,10,14,GREY)
    data=[["TIME","WHAT PULLED ME AWAY?","TRIGGER","ONE CHANGE TO TRY"]]+[["","","",""] for _ in range(6)]
    t=Table(data,colWidths=[25*mm,91*mm,65*mm,82*mm],rowHeights=[10*mm]+[18*mm]*6);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('TEXTCOLOR',(0,0),(-1,0),white),('GRID',(0,0),(-1,-1),.7,HexColor('#9caf9f')),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),3*mm)]));t.wrapOn(c,w,h);t.drawOn(c,16*mm,18*mm);c.showPage()

    w,h=header(c,"Weekly Review","Printable planner",5,total,True)
    prompts=["What moved forward?","When was focus easiest?","What distracted me most?","What can I remove or simplify?","What matters most next week?","One routine I will keep:"]
    xys=[(16,112),(151,112),(16,63),(151,63),(16,14),(151,14)]
    for p,(xm,yp) in zip(prompts,xys):
        c.setFillColor(PALE); c.roundRect(xm*mm,yp*mm,126*mm,42*mm,4*mm,fill=1,stroke=0); c.setFillColor(INK); c.setFont("Helvetica-Bold",10); c.drawString((xm+6)*mm,(yp+31)*mm,p); c.setStrokeColor(HexColor("#c2ccc4")); c.line((xm+6)*mm,(yp+17)*mm,(xm+120)*mm,(yp+17)*mm); c.line((xm+6)*mm,(yp+8)*mm,(xm+120)*mm,(yp+8)*mm)
    c.showPage()

    w,h=header(c,"Filled Example","Printable planner",6,total,True)
    c.setFillColor(MIST); c.roundRect(16*mm,h-115*mm,126*mm,48*mm,4*mm,fill=1,stroke=0); c.setFillColor(INK); c.setFont("Helvetica-Bold",12); c.drawString(23*mm,h-82*mm,"ONE MEANINGFUL OUTCOME"); para(c,"Send the revised proposal with a clear recommendation.",23*mm,h-90*mm,110*mm,11,15,INK)
    c.setFillColor(INK); c.setFont("Helvetica-Bold",12); c.drawString(158*mm,h-75*mm,"NEXT ACTIONS")
    actions=["Open the feedback notes","Revise scope and timeline","Write the recommendation email"]
    for i,a in enumerate(actions):
        y=h-(90+i*17)*mm; c.setStrokeColor(ORANGE); c.rect(159*mm,y,5*mm,5*mm,fill=0,stroke=1); c.setFillColor(GREY); c.setFont("Helvetica",10); c.drawString(169*mm,y+1*mm,a)
    c.setFillColor(PALE); c.roundRect(16*mm,22*mm,w-32*mm,64*mm,4*mm,fill=1,stroke=0); c.setFillColor(INK); c.setFont("Helvetica-Bold",11); c.drawString(23*mm,75*mm,"DISTRACTION DATA"); para(c,"10:20 - checked messages after a difficult paragraph. Change: keep messages closed until the 50-minute block ends.",23*mm,67*mm,w-46*mm,10,14,GREY); para(c,"14:05 - remembered an unrelated invoice. Change: write it in the capture lane and return to the plan.",23*mm,48*mm,w-46*mm,10,14,GREY)
    c.save()

reset_path=OUT/"the-focus-reset.pdf"; planner_path=OUT/"the-focus-planner.pdf"
reset_pdf(reset_path); planner_pdf(planner_path)
for p in (reset_path,planner_path): (COPY/p.name).write_bytes(p.read_bytes())
print(reset_path); print(planner_path)
