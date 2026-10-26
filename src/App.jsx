import { useEffect, useState } from "react";
import { ArrowDown, ArrowRight, CalendarDots, Check, CheckCircle, DownloadSimple, Leaf, ListChecks, ShieldCheck, Sparkle, Target, Timer, TrendUp, WarningCircle, X } from "@phosphor-icons/react";

const routes = new Set(["home", "thanks", "checkout", "success"]);

function useHashRoute() {
  const read = () => {
    const value = location.hash.replace("#/", "") || "home";
    return routes.has(value) ? value : "home";
  };
  const [route, setRoute] = useState(read);
  useEffect(() => {
    const onHash = () => setRoute(read());
    addEventListener("hashchange", onHash);
    return () => removeEventListener("hashchange", onHash);
  }, []);
  const go = (next) => {
    location.hash = `#/${next}`;
    scrollTo({ top: 0, behavior: "smooth" });
  };
  return [route, go];
}

function Brand() {
  return <a className="brand" href="#/home" aria-label="ClearFocus Studio home"><span />CLEARFOCUS STUDIO</a>;
}

function DemoNote() {
  return <div className="demo-note"><ShieldCheck size={18} weight="fill" /> Portfolio demo: forms are not saved or emailed, and checkout never charges you.</div>;
}

function Header() {
  return <>
    <DemoNote />
    <header className="site-header"><div className="shell nav-wrap">
      <Brand />
      <nav aria-label="Primary navigation">
        <a href="#inside">Inside the guide</a><a href="#preview">Preview</a><a href="#faqs">FAQs</a>
      </nav>
      <button className="button small" onClick={() => document.querySelector("#signup")?.scrollIntoView({ behavior: "smooth" })}>Get the free guide</button>
    </div></header>
  </>;
}

function SignupForm({ go, compact = false }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [errors, setErrors] = useState({});
  const submit = (e) => {
    e.preventDefault();
    const next = {};
    if (!compact && name.trim().length < 2) next.name = "Please enter your name.";
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) next.email = "Please enter a valid email.";
    setErrors(next);
    if (!Object.keys(next).length) go("thanks");
  };
  return <form className={`signup ${compact ? "compact" : ""}`} onSubmit={submit} noValidate>
    {!compact && <label>First name<input value={name} onChange={e => setName(e.target.value)} aria-invalid={!!errors.name} placeholder="Your first name" autoComplete="name" />{errors.name && <span className="field-error"><WarningCircle />{errors.name}</span>}</label>}
    <label>Email address<input value={email} onChange={e => setEmail(e.target.value)} aria-invalid={!!errors.email} placeholder="you@example.com" inputMode="email" autoComplete="email" />{errors.email && <span className="field-error"><WarningCircle />{errors.email}</span>}</label>
    <button className="button" type="submit">Get My Free Guide <ArrowRight weight="bold" /></button>
    <p>Free PDF. Practical advice you can use today.</p>
  </form>;
}

const benefits = [
  [Target, "Clear priorities", "Focus on what really moves your work forward."],
  [Leaf, "Fewer distractions", "Reduce what pulls your attention away."],
  [Sparkle, "A calmer routine", "Create a more focused and sustainable way of working."],
];

function Home({ go }) {
  return <div className="page home">
    <Header />
    <main>
      <section className="hero" id="signup"><div className="shell hero-grid">
        <div className="hero-copy"><p className="eyebrow">FREE GUIDE FOR INDEPENDENT PROFESSIONALS</p><h1>A clearer plan<br />for your workday.</h1><p className="lede">Set your priorities, reduce distractions and make room for meaningful work.</p><SignupForm go={go} /></div>
        <div className="hero-visual"><img src="assets/focus-reset-mockup.png" alt="The Focus Reset ebook and sample pages" /></div>
      </div></section>

      <section className="benefit-strip"><div className="shell three-cols">{benefits.map(([Icon, title, copy]) => <article key={title}><Icon size={38} weight="regular" /><div><h3>{title}</h3><p>{copy}</p></div></article>)}</div></section>

      <section className="section problem"><div className="shell"><div className="section-heading"><h2>Busy all day. Still not moving forward?</h2><p>It is easy to feel busy without making real progress. These familiar patterns quietly fragment a thoughtful workday.</p></div><div className="card-grid">
        {[[ListChecks,"Too many competing tasks","Client work, admin and new opportunities can make it hard to know what to focus on."],[Timer,"Constant interruptions","Messages, emails and notifications can break your concentration throughout the day."],[WarningCircle,"No clear plan for the day","Without a simple structure, it is easy to drift from one task to another."]].map(([I,t,c])=><article className="outline-card" key={t}><span className="icon-orb"><I size={24}/></span><h3>{t}</h3><p>{c}</p></article>)}
      </div></div></section>

      <section className="section inside" id="inside"><div className="shell"><div className="section-heading"><h2>Inside The Focus Reset</h2><p>A practical guide to help you plan your work, protect your attention and make steady progress.</p></div><div className="card-grid inside-grid">
        {[[ListChecks,"Choose what matters","Identify your priorities and turn them into clear next steps."],[ShieldCheck,"Protect your attention","Reduce common distractions and create space to focus."],[CalendarDots,"Build a workable routine","Plan focused sessions around the way you work."]].map(([I,t,c])=><article className="solid-card" key={t}><span className="dark-orb"><I size={25}/></span><h3>{t}</h3><p>{c}</p></article>)}
      </div></div></section>

      <section className="section preview" id="preview"><div className="shell preview-grid"><div className="spread" role="img" aria-label="A preview of two pages inside The Focus Reset"><div className="paper"><span>CHAPTER 1</span><h3>Choose the work<br />that matters</h3><p>Not everything on your to-do list is equally important. Prioritising helps you focus on the work that moves you forward.</p>{["List your commitments","Choose one meaningful outcome","Break it into a clear action"].map((x,i)=><div className="step" key={x}><b>{i+1}</b><strong>{x}</strong></div>)}</div><div className="paper"><span>CHAPTER 2</span><h3>A simple way to prioritise</h3><p>Use the matrix to think about your tasks and choose what is important.</p><div className="matrix"><b>Schedule</b><b>Do now</b><b>Remove</b><b>Delegate</b></div></div></div><div className="preview-copy"><h2>A practical<br />look inside</h2>{["Clear explanations.","Practical examples.","Useful exercises."].map(x=><p className="check-line" key={x}><CheckCircle weight="fill" />{x}</p>)}<p className="body-copy">The Focus Reset gives you simple frameworks and exercises to help you prioritise your work, reduce distractions and build a routine that fits your life.</p></div></div></section>

      <section className="section steps-section"><div className="shell"><div className="section-heading"><h2>Three steps to a clearer workday</h2><p>Get your free guide and start putting ideas into practice today.</p></div><div className="steps-row">{[[DownloadSimple,"Download your guide","Enter your details and get instant access to the PDF."],[ListChecks,"Choose one idea to try","Pick a strategy that feels most relevant to you right now."],[TrendUp,"Put it into practice","Apply it to your work and notice the difference over time."]].map(([I,t,c],i)=><article key={t}><span className="icon-orb"><I size={26}/></span><b className="step-no">{i+1}</b><div><h3>{t}</h3><p>{c}</p></div></article>)}</div><button className="button centered" onClick={()=>document.querySelector("#signup")?.scrollIntoView({behavior:"smooth"})}>Get My Free Guide</button></div></section>

      <section className="section faqs" id="faqs"><div className="shell narrow"><div className="section-heading"><h2>A few quick answers</h2></div>{[["Who is this guide for?","Independent professionals who want a simpler way to organise their work."],["Is the guide free?","Yes. You can download the PDF at no cost."],["What is included?","Practical guidance, examples and exercises to help you plan focused work."],["Can I use it at my own pace?","Yes. Start with one section and return whenever you need it."]].map(([q,a])=><details key={q}><summary>{q}<ArrowDown /></summary><p>{a}</p></details>)}</div></section>

      <section className="final-cta"><div className="shell cta-grid"><img src="assets/focus-reset-mockup.png" alt="The Focus Reset guide" /><div><h2>Make space for your next priority.</h2><p>Start with a simple, practical guide to a more focused workday.</p><SignupForm go={go} compact /></div></div></section>
    </main>
    <Footer />
  </div>;
}

function FunnelShell({ children, title = "" }) {
  return <div className="funnel-page"><DemoNote /><header className="simple-header"><div className="shell"><Brand /><span>{title}</span></div></header>{children}<Footer /></div>;
}

function Thanks({ go }) {
  return <FunnelShell title="Your download is ready"><main>
    <section className="thanks-hero"><div className="shell"><span className="success-mark"><Check size={34} weight="bold" /></span><p className="eyebrow">THANK YOU</p><h1>Your Focus Reset is ready.</h1><p>Download the guide now. Your details were validated only in the page and were not saved or sent anywhere.</p><a className="button" href="downloads/the-focus-reset.pdf" download><DownloadSimple /> Download The Focus Reset</a></div></section>
    <section className="upsell"><div className="shell upsell-grid"><div className="upsell-image"><img src="assets/focus-planner-mockup.png" alt="The Focus Planner with sample printable pages" /></div><div className="upsell-copy"><p className="eyebrow">OPTIONAL ONE-TIME OFFER</p><h2>Turn focused ideas into a plan you can use.</h2><p>The Focus Planner gives you a calm, repeatable system for choosing priorities, protecting focus time and learning from distractions.</p><ul>{["Daily focus planning page","Weekly overview and review","Distraction log","Filled example to get you started","Reusable printable PDF"].map(x=><li key={x}><CheckCircle weight="fill" />{x}</li>)}</ul><div className="price"><small>THE FOCUS PLANNER</small><strong>US$19</strong><span>one-time demo purchase</span></div><button className="button wide" onClick={()=>go("checkout")}>Get The Focus Planner <ArrowRight /></button><button className="text-link" onClick={()=>document.querySelector("#free-download")?.scrollIntoView({behavior:"smooth"})}>No thanks, keep my free guide</button></div></div></section>
    <section id="free-download" className="free-reminder"><div className="shell"><DownloadSimple size={30}/><div><h3>Your free guide is yours either way.</h3><p>Skipping the planner does not affect your download.</p></div><a href="downloads/the-focus-reset.pdf" download>Download free Ebook</a></div></section>
  </main></FunnelShell>;
}

function Checkout({ go }) {
  const [agreed, setAgreed] = useState(false);
  const [showError, setShowError] = useState(false);
  const complete = () => { if (!agreed) return setShowError(true); go("success"); };
  return <FunnelShell title="Demo checkout"><main className="checkout"><div className="shell checkout-grid"><section className="checkout-main"><p className="eyebrow">SIMULATED CHECKOUT</p><h1>Complete your demo order</h1><div className="notice"><ShieldCheck size={24} weight="fill" /><div><strong>No payment is collected.</strong><p>This is a portfolio demonstration. There are no card fields, no account creation and no real charge.</p></div></div><label className="agreement"><input type="checkbox" checked={agreed} onChange={e=>{setAgreed(e.target.checked);setShowError(false)}} /><span><b>I understand this is a simulated purchase.</b><small>Clicking the button only unlocks the sample Planner download page.</small></span></label>{showError && <p className="checkout-error"><WarningCircle /> Please confirm the demo notice to continue.</p>}<button className="button wide" onClick={complete}>Simulate purchase <ArrowRight /></button><button className="text-link" onClick={()=>go("thanks")}><X /> Cancel and return to free download</button></section><aside className="order-card"><img src="assets/focus-planner-mockup.png" alt="The Focus Planner" /><h2>Order summary</h2><div><span>The Focus Planner</span><b>US$19.00</b></div><p>Printable PDF · Instant demo access</p><hr /><div className="total"><span>Total</span><b>US$19.00</b></div><small>Simulated only — you will not be charged.</small></aside></div></main></FunnelShell>;
}

function Success({ go }) {
  return <FunnelShell title="Demo purchase complete"><main className="purchase-success"><div className="shell success-grid"><div><span className="success-mark"><Check size={34} weight="bold" /></span><p className="eyebrow">DEMO PURCHASE COMPLETE</p><h1>Your Focus Planner is ready.</h1><p>No money was charged and no personal information was collected. Download the complete printable planner below.</p><a className="button" href="downloads/the-focus-planner.pdf" download><DownloadSimple /> Download The Focus Planner</a><button className="text-link home-link" onClick={()=>go("home")}>Return to homepage <ArrowRight /></button></div><img src="assets/focus-planner-mockup.png" alt="The Focus Planner printable set" /></div></main></FunnelShell>;
}

function Footer() {
  return <footer><div className="shell"><Brand /><p>Independent portfolio demonstration. No data is stored; no purchase is processed.</p><a href="#/home">Home</a></div></footer>;
}

export function App() {
  const [route, go] = useHashRoute();
  if (route === "thanks") return <Thanks go={go} />;
  if (route === "checkout") return <Checkout go={go} />;
  if (route === "success") return <Success go={go} />;
  return <Home go={go} />;
}

