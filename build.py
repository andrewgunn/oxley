#!/usr/bin/env python3
"""Generates the static Oxley preview site. Run: python3 build.py"""
import os
from html import escape

LIVE = "https://oxleymortgages.co.uk"
PHONE = "01246 551 155"
TEL = "tel:01246551155"
EMAIL = "hello@oxleymortgages.co.uk"
CAL_CALL = "https://calendly.com/george-oxleymortgages/30min"
CAL_VISIT = "https://calendly.com/george-oxleymortgages/1-hour-in-person-chat"

I = {
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0116 0"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9L12 3z"/>',
    "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 012-2h2a2 2 0 012 2v2M3 13h18"/>',
    "card": '<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6 15h4"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
    "box": '<path d="M3 8l9-5 9 5v8l-9 5-9-5V8z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
    "build": '<path d="M3 21h18M5 21V10l7-6 7 6v11"/><path d="M10 21v-6h4v6"/><path d="M15 3h4v4"/>',
    "btl": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2M11 21v-3h2v3"/>',
    "refresh": '<path d="M20 11a8 8 0 00-14.6-4.5L3 9M4 13a8 8 0 0014.6 4.5L21 15"/><path d="M3 4v5h5M21 20v-5h-5"/>',
    "help": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M9.5 15.5l2 2 3.5-4"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
    "fb": '<path d="M14 8h3V4h-3a4 4 0 00-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/>',
}


def ico(name, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[name]}</svg>'


SERVICES = [
    dict(slug="self-employed-mortgages", name="Self Employed Mortgages", icon="brief", img="self-employed.webp",
         blurb="Sole traders, directors, contractors and the newly self-employed — with as little as one year's accounts.",
         h1="Mortgages for the self-employed",
         lede="If you're self-employed or run your own business, arranging a mortgage can feel more complex than it needs to be. Lenders often assess income differently for business owners, which is why specialist advice can make all the difference.",
         body=[("", ["As experienced mortgage advisers based in Chesterfield, Derbyshire, we help self-employed applicants understand their options and secure mortgages that suit their circumstances. Whether you're buying your first home, moving house, or refinancing, we'll guide you through the process from start to finish."]),
               ("We regularly support clients who are", ["@checks:Newly self-employed with as little as one year's accounts|CIS contractors|Company directors|Sole traders|Business partners|Limited company owners"]),
               ("Securing a mortgage as a business owner", ["Preparation is key when applying for a mortgage while self-employed. Lenders will usually want to see clear evidence of income, so having documents such as accounts, SA302s, tax year overviews, and bank statements ready can significantly speed things up.",
                                                           "Working closely with an accountant can also be beneficial, ensuring your income is presented accurately and in a way lenders understand. This is particularly important if your earnings fluctuate or are drawn from multiple sources.",
                                                           "Although self-employed applicants may encounter tighter criteria, there are lenders who specialise in this area and offer competitive mortgage deals. With the right guidance and access to specialist lenders, being self-employed doesn't have to be a barrier to homeownership.",
                                                           "By choosing a knowledgeable mortgage broker who understands self-employed income, you'll be in a stronger position to secure the right mortgage for your needs."])]),
    dict(slug="bad-credit-mortgages", name="Bad Credit Mortgages", icon="card", img="bad-credit.webp",
         blurb="CCJs, defaults, DMPs or missed payments? Specialist lenders look at the whole picture, not just a score.",
         h1="Bad &amp; poor credit mortgage advice in Chesterfield",
         lede="Having a less-than-perfect credit history doesn't mean homeownership is out of reach. Many people experience financial setbacks at some point, and specialist mortgage advice can make a real difference when it comes to moving forward.",
         body=[("", ["As experienced mortgage advisers based in Chesterfield, we work with a wide range of lenders who consider more than just your credit score. Our role is to understand your situation, explain your options clearly, and help you find a mortgage that fits your circumstances."]),
               ("We regularly help clients with", ["@checks:County Court Judgments (CCJs)|Defaults|Debt Management Plans (DMPs)|Missed or late payments|Previous IVAs or bankruptcy|Little or limited credit history"])],
         faq=[("What is a bad credit mortgage?", "A bad credit mortgage is designed for applicants whose credit history may make it difficult to secure a standard mortgage. These mortgages are offered by specialist lenders who take a broader view of your finances, looking at affordability, stability, and recent conduct rather than past issues alone."),
              ("Can I get a mortgage with bad credit?", "In many cases, yes. While high-street lenders can be strict, there are specialist lenders who are more flexible. Factors such as how long ago the credit issues occurred, whether they've been resolved, and your current financial position all play a key role in determining your eligibility."),
              ("How do you get approved for a bad credit mortgage?", "Preparation is essential. Having up-to-date documents, demonstrating stable income, managing your current credit well, and reducing outstanding debts where possible can all improve your chances. Working with a mortgage broker who understands bad credit lending gives you access to lenders best suited to your situation."),
              ("How much can you borrow with a poor credit history?", "The amount you can borrow will depend on your income, outgoings, deposit size, and the severity of your credit issues. Some lenders may offer lower loan-to-income multiples, while others may be more generous if the credit problems are historic and your finances are now stable."),
              ("How does a partner's bad credit affect a joint application?", "When applying jointly, both applicants' credit histories are considered. If one partner has poor credit, it can limit the lender options available. In some cases, applying in one name or using a specialist lender may be more suitable — something a mortgage adviser can help assess.")]),
    dict(slug="first-time-buyer-mortgages", name="First Time Buyer Mortgages", icon="key", img="first-time.webp",
         blurb="Clear, jargon-free guidance from your first question to getting the keys.",
         h1="Mortgages for first-time buyers",
         lede="Taking your first step onto the property ladder is an exciting milestone, but it can also feel overwhelming. With so many decisions to make and unfamiliar terms to navigate, having the right support from the outset makes the process far smoother.",
         body=[("", ["We provide clear, practical mortgage advice for first-time buyers across Chesterfield and Derbyshire, helping you understand your options and move forward with confidence. From your initial enquiry through to completion, we'll be there to guide you every step of the way."]),
               ("Getting started as a first-time buyer", ["Before you begin viewing properties, it's important to understand what you can realistically afford and what lenders are likely to offer. Speaking to a mortgage adviser early on puts you in a strong position when the right home comes along.",
                                                         "At your initial appointment, your mortgage adviser will take time to review your income, regular outgoings, and financial commitments. This allows us to help you set a sensible budget and avoid overstretching yourself."]),
               ("Understanding the mortgage process", ["Your adviser will explain how much you may be able to borrow, what your estimated monthly payments could look like, and what happens at each stage of the buying journey. We'll also outline the steps involved after an offer is accepted, so you know exactly what to expect.",
                                                      "In addition, we'll make sure you're fully aware of all the costs associated with buying a home — such as deposits, legal fees, surveys, and lender charges — and when these payments are typically required.",
                                                      "With straightforward advice and ongoing support, we aim to make your first home purchase as smooth and stress-free as possible."])]),
    dict(slug="moving-house-mortgages", name="Moving House Mortgages", icon="box", img="moving.webp",
         blurb="Upsizing, downsizing or relocating — get your finances lined up before you make an offer.",
         h1="Mortgages for moving home",
         lede="Moving home is a major step, whether you're upsizing, downsizing, or relocating. Alongside choosing the right property, there are important financial decisions to consider, and understanding your mortgage options early helps everything run more smoothly.",
         body=[("", ["Expert mortgage advice can help you navigate the many factors involved in selling your current home and purchasing a new one. From assessing affordability to reviewing lender criteria, support at the right time can make a significant difference."]),
               ("Where to start when moving home", ["Before committing to a move, it's important to understand the full picture. This includes the costs involved in both selling and buying a property, such as legal fees, estate agent charges, surveys, and mortgage-related costs — as well as when these payments are typically required.",
                                                   "If you already have a mortgage, there may also be early repayment charges to consider. In some cases, your existing mortgage could be portable, while in others, a new deal may be more suitable. As lending criteria and mortgage products change frequently, options that were available in the past may no longer apply."]),
               ("Preparing for your next purchase", ["Taking advice before your property sale is agreed can put you in a stronger position once an offer is accepted. Understanding how much you can borrow and what lenders are currently offering allows you to move quickly and confidently when the time comes to make an offer on your next home.",
                                                     "With the right preparation and guidance, your move can be planned with clarity and confidence, helping you transition smoothly into your next property."])]),
    dict(slug="new-build-house-mortgages", name="New Build House Mortgages", icon="build", img="new-build.webp",
         blurb="Tight timelines and lender-specific criteria, handled from reservation to completion.",
         h1="New build property mortgages",
         lede="Buying a new build home comes with its own set of considerations, whether you're purchasing your very first property or moving from an existing home. From tighter timelines to lender-specific criteria, specialist mortgage advice helps keep everything on track.",
         body=[("", ["Support throughout the buying process helps you understand how new build mortgages work, what lenders require, and how to prepare financially. With the right guidance, you can move forward confidently from reservation through to completion."])]),
    dict(slug="buy-to-let-mortgages", name="Buy to Let Mortgages", icon="btl", img="buy-to-let.webp",
         blurb="Your first rental or a growing portfolio — lending based on rent as well as income.",
         h1="Buy to let mortgages",
         lede="Purchasing a property as an investment requires a different approach to residential lending. Buy to let mortgages are assessed based on rental income as well as your personal financial position, which is why tailored advice is essential.",
         body=[("", ["Whether you're exploring buy to let for the first time or expanding an existing portfolio, specialist guidance can help you understand lender expectations, deposit requirements, and potential returns.",
                     "@notice:Please note: not all buy to let mortgages are regulated by the Financial Conduct Authority."])]),
    dict(slug="remortgaging-advice", name="Remortgaging Advice", icon="refresh", img="remortgage.webp",
         blurb="Fixed rate ending? We'll compare your current deal with the whole market.",
         h1="Remortgaging your home",
         lede="Reviewing your mortgage doesn't have to be complicated. Whether you're approaching the end of a fixed term or considering raising additional funds, understanding your options can save you money and help you make the right decisions.",
         body=[("What remortgaging involves", ["Remortgaging is the process of switching your current mortgage to a new deal, either with your existing lender or a different one. Even if your current payments have reduced over time, it's still worth reviewing your mortgage to ensure it continues to meet your needs and long-term goals.",
                                              "For homeowners whose property has increased in value, remortgaging can also provide an opportunity to release additional funds for home improvements, debt consolidation, or other priorities."]),
               ("Choosing the right mortgage deal", ["When considering a new mortgage, it's important to look beyond the headline rate. Other factors, such as lender fees, the most suitable mortgage term, and the type of mortgage that aligns with your goals, should all be taken into account.",
                                                    "Specialist advice can help you navigate these details and compare your current deal with what's available on the market. By doing so, you can identify the mortgage that best suits your circumstances."]),
               ("Support throughout the process", ["From initial review to application and completion, expert guidance ensures the remortgaging process is smooth and straightforward. Advisers can assess your current mortgage, explore available products, and provide clear recommendations so you can make informed decisions with confidence."])]),
    dict(slug="help-to-buy-scheme", name="Help to Buy Scheme", icon="help", img="help-to-buy.webp",
         blurb="How the (now closed) equity loan worked, and other routes for small-deposit new build buyers.",
         h1="Help to Buy scheme information",
         lede="The Help to Buy: Equity Loan scheme (now expired) was designed to support buyers purchasing new build homes with a smaller deposit. Buyers could combine a mortgage and personal deposit with an equity loan, reducing the amount needed from a lender.",
         body=[("", ["For an initial period, no interest was charged on the equity loan, though the loan always remained repayable as a percentage of the property's value at the time of sale or repayment. This means the amount repaid could be higher or lower than the original loan, depending on property value changes."]),
               ("How the Help to Buy scheme worked", ["The equity loan could be up to 20% of the property value (or up to 40% in Greater London, reflecting higher property prices), with buyers contributing a minimum personal deposit of 5%, subject to scheme rules and regional limits.",
                                                     "Eligibility depended on factors such as property value, buyer status, and location. Mortgage advice played an important role in confirming whether buyers qualified, how much they could afford, and which lenders supported the scheme."]),
               ("Other options for buying a new build home", ["Help to Buy was not the only route available to buyers with smaller deposits. Other mortgage products may be suitable, although some lenders place restrictions on new build properties, particularly where deposits are 10% or less.",
                                                             "Because criteria can vary significantly between lenders, specialist advice helps identify suitable options and navigate any limitations that apply specifically to new build purchases."])]),
]

TEAM = [
    dict(name="Mat Barnes", img="mat.webp", role="Mortgage adviser · since 1997",
         bio="I've been in the property & mortgage market since leaving school – so it's in my bones! Since 1997 I've been running my own mortgage business in Chesterfield alongside Hunters Estate Agency. I'm fanatic about customer service & getting the YES for all my customers!",
         fun="For fun I enjoy travel, watching rugby & playing really bad golf!"),
    dict(name="George Barnes", img="george.webp", role="Mortgage adviser · since 2019",
         bio="I have been providing my clients with expert mortgage advice since 2019 & worked in the property industry since 2015. Striving to bring modern methods, efficiency & accountability to the mortgage industry. Providing the YES! to all my customers new & old.",
         fun="Passionate about whippets, hiking, cars, music & of course mortgages."),
    dict(name="Craig Swan", img="craig.webp", role="Mortgage adviser · 30+ years",
         bio="I've been advising people on mortgages for decades! Working alongside Mat for the last 30 years I have organised literally thousands of mortgages for all sorts of cases. It's all I do – so I am sure I can help! Just give me a call!",
         fun="For fun I like to meet up with friends & socialise — the odd tot of whisky may be involved!"),
]

REVIEWS = [
    ("Emma C", "We honestly couldn't have asked for a better mortgage advisor than George. From the very beginning, he went above and beyond to make what could have been a stressful process feel smooth and manageable. He genuinely worked hard to secure the best possible outcome for us."),
    ("Dan Cooper", "I cannot speak highly enough of Kim and George. They are first class. Great advice and easy to work with. They were calm and patient throughout."),
    ("Frankie", "Excellent friendly service, Craig and Kim are always very helpful and explain every step of the mortgage process. We have been using Craig for years to arrange our mortgages and buy to let mortgages and wouldn't go anywhere else."),
    ("Jessica Woodcroft", "George is absolutely fantastic! Very fast and efficient! Booked an appointment with him on the same day of looking for someone, and a later appointment in the day which was perfect for me, and not what everyone offers!"),
    ("Anne Crane", "George and Kim have both been amazing to work with. They have made a stressful and complicated process very straightforward and easy. I really don't like filling in forms or getting quotes, and they just took care of it all."),
    ("Ed Green", "Would recommend. A massive thank you to George B in particular, he helped us massively as first time buyers, we are very grateful!"),
    ("Emily May", "George was fantastic! From the moment I reached out, to the final email saying congratulations on completing, he was fab from start to finish! His knowledge is unmatched. Highly highly recommended!! 10/10!"),
    ("Lynne Bird", "Very helpful and gave advice around aspects I hadn't considered. Flexible with appointments. Worthwhile."),
]

YES = [
    ("Expert mortgage advisers", "Unbiased recommendations tailored to your goals, not a lender's agenda."),
    ("Same day appointments", "Speak to an adviser quickly so you can take action without delays."),
    ("Adverse credit mortgages", "We help clients with past credit issues secure realistic, achievable mortgages."),
    ("Self employed mortgages", "Clear guidance and lender choices that make proving your income straightforward."),
    ("Rated 5 stars", "Our clients trust us for honest advice, smooth applications and reliable results."),
    ("Family run business", "A friendly, personal service where you're treated like one of our own, not a number."),
]

POSTS = [
    ("2026/09/22/remortgaging-explained-simply-when-should-you-remortgage", "Remortgaging", "22 Sep 2026", "Remortgaging explained simply: when should you remortgage?", "If you already own your home, you may have heard the term 'remortgaging' — here's when it makes sense.", "post-remortgaging.webp"),
    ("2026/09/03/from-tenant-to-homeowner-how-to-get-mortgage-ready", "First-time buyers", "3 Sep 2026", "From tenant to homeowner: how to get mortgage ready", "For many people, renting is the first step towards having a place they can call their own.", "post-tenant.webp"),
    ("2026/07/20/common-reasons-mortgage-applications-are-declined-and-how-to-avoid-them", "Applications", "20 Jul 2026", "Common reasons mortgage applications are declined (and how to avoid them)", "Applying for a mortgage is an exciting step. Here's how to avoid the most common pitfalls.", "post-declined.webp"),
    ("2026/06/24/fixed-rate-or-tracker-mortgage-understanding-your-options-in-2026", "Guides", "24 Jun 2026", "Fixed rate or tracker mortgage? Understanding your options in 2026", "Choosing a mortgage is about more than simply finding the lowest interest rate.", "post-fixed.webp"),
    ("2026/06/08/one-year-self-employed-you-may-still-be-able-to-get-a-mortgage", "Self-employed", "8 Jun 2026", "One year self-employed? You may still be able to get a mortgage", "One of the most common misconceptions is that you need several years of accounts.", "self-employed.webp"),
    ("2026/05/18/what-lenders-really-look-for-if-you-have-bad-credit", "Bad credit", "18 May 2026", "What lenders really look for if you have bad credit", "Having bad credit doesn't automatically mean you won't be able to get a mortgage.", "bad-credit.webp"),
    ("2026/04/28/how-to-prepare-for-a-mortgage-application-in-2026", "Applications", "28 Apr 2026", "How to prepare for a mortgage application in 2026", "Cut through the conflicting information online with a simple preparation checklist.", "post-prepare.webp"),
    ("2026/02/13/welcome-to-oxley-mortgage-solutions-your-path-to-a-yes-made-simple", "News", "13 Feb 2026", "Welcome to Oxley Mortgage Solutions — your path to a “YES” made simple", "Introducing Oxley, an independent mortgage brokerage based in Chesterfield.", "team.webp"),
    ("2026/02/03/why-being-self-employed-doesnt-mean-no-mortgage", "Self-employed", "3 Feb 2026", "Why being self-employed doesn't mean no mortgage", "Applying as self-employed can feel like an uphill battle. It doesn't have to be.", "office-2.webp"),
    ("2026/01/27/how-oxley-mortgage-solutions-supports-first-time-buyers", "First-time buyers", "27 Jan 2026", "How Oxley Mortgage Solutions supports first time buyers", "Buying your first home is exciting, but it can also feel confusing. Here's how we help.", "first-time.webp"),
]


# ---------- partials ----------

def head(r, title, desc, path):
    return f"""<!doctype html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{escape(desc)}">
<!-- Design preview only: keep out of search results so the live site's SEO is untouched -->
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<link rel="canonical" href="{LIVE}/{path}">
<meta name="theme-color" content="#221f46">
<link rel="icon" href="{r}assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Domine:wght@600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(r, current):
    menu = "".join(f'<a href="{r}{s["slug"]}/"><span class="ico">{ico(s["icon"])}</span>{s["name"]}</a>' for s in SERVICES)
    dmenu = "".join(f'<a href="{r}{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)
    is_mort = current == "mortgages" or current in [s["slug"] for s in SERVICES]

    def nl(slug, label):
        cur = ' aria-current="page"' if current == slug else ""
        return f'<a class="nav__link" href="{r}{slug + "/" if slug else ""}"{cur}>{label}</a>'
    return f"""<div class="preview-flag">Design preview — the live website is <a href="{LIVE}/">oxleymortgages.co.uk</a></div>
<div class="topbar"><div class="wrap">
  <div class="topbar__left">
    <a class="topbar__item" href="{TEL}">{ico("phone")}{PHONE}</a>
    <a class="topbar__item topbar__hide-sm" href="mailto:{EMAIL}">{ico("mail")}{EMAIL}</a>
  </div>
  <div class="topbar__item topbar__hide-sm"><span class="topbar__stars">★★★★★</span> Rated Excellent on Google</div>
</div></div>
<header class="header"><div class="wrap">
  <a class="logo" href="{r}" aria-label="Oxley Mortgage Solutions — home"><img src="{r}assets/img/logo.png" alt="Oxley Mortgage Solutions" width="774" height="319"></a>
  <nav class="nav" aria-label="Main">
    {nl("", "Home")}
    {nl("about-oxley", "About")}
    <div class="nav__item">
      <button class="nav__toggle{' is-current' if is_mort else ''}" aria-expanded="false" aria-haspopup="true">Mortgages {ico("chev")}</button>
      <div class="nav__menu">{menu}<div class="nav__menu-all"><a href="{r}mortgages/">View all mortgage options {ico("arrow")}</a></div></div>
    </div>
    {nl("help-advice", "Help &amp; Advice")}
    {nl("contact-oxley-mortgages", "Contact")}
  </nav>
  <div class="header__actions">
    <a class="btn btn--ghost btn--sm" href="{TEL}">{ico("phone")}Call us</a>
    <a class="btn btn--sm" href="{CAL_CALL}" target="_blank" rel="noopener">Book a call</a>
    <button class="burger" data-drawer-open aria-controls="drawer" aria-expanded="false" aria-label="Open menu">{ico("menu")}</button>
  </div>
</div></header>
<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer__scrim" data-drawer-close></div>
  <div class="drawer__panel" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="drawer__head"><img src="{r}assets/img/logo.png" alt="Oxley Mortgage Solutions"><button class="burger" style="display:inline-flex" data-drawer-close aria-label="Close menu">{ico("close")}</button></div>
    <nav aria-label="Mobile">
      <a href="{r}">Home</a>
      <a href="{r}about-oxley/">About Oxley</a>
      <details{' open' if is_mort else ''}><summary>Mortgages {ico("chev")}</summary><div>{dmenu}<a href="{r}mortgages/"><strong>All mortgage options</strong></a></div></details>
      <a href="{r}help-advice/">Help &amp; Advice</a>
      <a href="{r}contact-oxley-mortgages/">Contact</a>
    </nav>
    <div class="drawer__foot">
      <a class="btn" href="{CAL_CALL}" target="_blank" rel="noopener">{ico("cal")}Book a call</a>
      <a class="btn btn--yellow" href="{TEL}">{ico("phone")}{PHONE}</a>
      <p>Same-day appointments, Monday to Friday</p>
    </div>
  </div>
</div>
<main id="main">
"""


def cta_band(r):
    return f"""<section class="section"><div class="wrap"><div class="cta reveal">
  <div><span class="eyebrow">Let's talk</span><h2>Ready to get your “YES”?</h2>
  <p>A friendly, no-pressure chat with one of our advisers is all it takes to get started. Same-day appointments available.</p></div>
  <div class="btn-row"><a class="btn btn--yellow" href="{CAL_CALL}" target="_blank" rel="noopener">{ico("cal")}Book a call</a><a class="btn btn--ghost" href="{TEL}">{ico("phone")}{PHONE}</a></div>
</div></div></section>
"""


def footer(r):
    links = "".join(f'<li><a href="{r}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES[:7])
    return f"""</main>
<footer class="footer">
  <div class="wrap footer__grid">
    <div class="footer__brand">
      <img src="{r}assets/img/logo-white.png" alt="Oxley Mortgage Solutions" width="773" height="319">
      <p>Search 1,000s of mortgages by spending 15 minutes talking to 1 adviser. A family-run brokerage in Chesterfield, helping people get to “YES”.</p>
      <a class="social" href="https://www.facebook.com/OxleyMortgageSolutions" aria-label="Oxley on Facebook" rel="noopener">{ico("fb")}</a>
    </div>
    <div><h4>Mortgages</h4><ul>{links}</ul></div>
    <div><h4>Oxley</h4><ul>
      <li><a href="{r}">Home</a></li><li><a href="{r}about-oxley/">About us</a></li><li><a href="{r}mortgages/">All mortgages</a></li>
      <li><a href="{r}help-advice/">Help &amp; Advice</a></li><li><a href="{r}contact-oxley-mortgages/">Contact</a></li></ul></div>
    <div><h4>Get in touch</h4><ul class="footer__contact">
      <li>{ico("pin")}<address>Unit 4, The Glass Yard<br>Sheffield Rd, Chesterfield<br>S41 8JY</address></li>
      <li>{ico("phone")}<a href="{TEL}">{PHONE}</a></li>
      <li>{ico("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{ico("clock")}<span>Monday to Friday</span></li></ul></div>
  </div>
  <div class="wrap legal">
    <p class="legal__warn">Your home may be repossessed if you do not keep up repayments on your mortgage.</p>
    <p>There may be a fee for mortgage advice. The fee is up to 1% but a typical fee is 0.3% of the amount borrowed.</p>
    <p>Oxley Mortgage Solutions Ltd is an appointed representative of Mortgage Advice Bureau (Derby) Limited which is authorised and regulated by the Financial Conduct Authority.</p>
    <p>Oxley Mortgage Solutions Ltd. Registered Office: Unit 4, The Glass Yard, Sheffield Road, Chesterfield, Derbyshire, S41 8JY. Registered in England Number: 16497554.</p>
    <div class="legal__bottom">
      <span>© <span data-year>2026</span> Oxley Mortgage Solutions Ltd</span>
      <ul><li><a href="{LIVE}/cookie-policy-uk/">Cookies</a></li><li><a href="{LIVE}/privacy-policy-2/">Privacy</a></li><li><a href="{LIVE}/your-rights/">Your rights</a></li>
      <li><a href="https://mortgageadvicebureau-privacy.my.onetrust.com/incident-portal/webforms/2cf3bbcb-5488-430c-bb3d-69383d968fa5/5a75de46-dcd1-410a-a5b1-3bdb2ec854ee" rel="noopener">Report a data-related complaint</a></li></ul>
    </div>
  </div>
</footer>
<div class="mobile-bar"><a class="btn btn--yellow" href="{TEL}">{ico("phone")}Call</a><a class="btn" href="{CAL_CALL}" target="_blank" rel="noopener">{ico("cal")}Book a call</a></div>
<script src="{r}assets/js/site.js" defer></script>
</body>
</html>
"""


def page(r, current, title, desc, path, body):
    return head(r, title, desc, path) + header(r, current) + body + footer(r)


def service_cards(r, items=SERVICES):
    return "".join(f'''<a class="card reveal" href="{r}{s["slug"]}/"><span class="ico">{ico(s["icon"])}</span><h3>{s["name"]}</h3><p>{s["blurb"]}</p><span class="card__more">Find out more {ico("arrow")}</span></a>''' for s in items)


def yes_grid():
    return '<div class="yes-grid reveal">' + "".join(f'<div class="yes"><span class="yes__tag">YES</span><h3>{t}</h3><p>{d}</p></div>' for t, d in YES) + "</div>"


def team_cards(r):
    return '<div class="team">' + "".join(f'''<article class="person reveal"><div class="person__img"><img src="{r}assets/img/{p["img"]}" alt="{p["name"]}" loading="lazy" width="600" height="650"></div>
<div class="person__body"><h3>{p["name"]}</h3><div class="person__role">{p["role"]}</div><p>{p["bio"]}</p><p class="person__fun">{p["fun"]}</p>
<a class="btn btn--ghost btn--sm" href="{CAL_CALL}" target="_blank" rel="noopener">Book with {p["name"].split()[0]}</a></div></article>''' for p in TEAM) + "</div>"


G_LOGO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.5 12.3c0-.8-.1-1.5-.2-2.2H12v4.2h5.9a5 5 0 01-2.2 3.3v2.7h3.5c2.1-1.9 3.3-4.7 3.3-8z"/><path fill="#34A853" d="M12 23c3 0 5.4-1 7.2-2.7l-3.5-2.7c-1 .7-2.2 1-3.7 1-2.9 0-5.3-1.9-6.2-4.5H2.2v2.8A11 11 0 0012 23z"/><path fill="#FBBC05" d="M5.8 14.1a6.6 6.6 0 010-4.2V7.1H2.2a11 11 0 000 9.8l3.6-2.8z"/><path fill="#EA4335" d="M12 5.4c1.6 0 3 .6 4.2 1.6l3.1-3.1A11 11 0 002.2 7.1l3.6 2.8C6.7 7.3 9.1 5.4 12 5.4z"/></svg>'


def reviews():
    cards = "".join(f'''<figure class="review"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>“{escape(t)}”</blockquote>
<footer><span class="review__avatar">{n[0]}</span><div><strong>{n}</strong><span>Google review</span></div></footer></figure>''' for n, t in REVIEWS)
    return f'''<section class="section section--sand" id="reviews"><div class="wrap">
<div class="reviews-head"><div><span class="eyebrow">Reviews</span><h2>Don't just take our word for it</h2></div>
<div class="rating"><span class="rating__g">{G_LOGO}</span><div><strong>Excellent</strong> <span class="stars">★★★★★</span><small>Based on 64 Google reviews</small></div></div></div>
<div class="reviews" tabindex="0" aria-label="Customer reviews">{cards}</div></div></section>
'''


def posts(r, items):
    return "".join(f'''<a class="post reveal" href="{LIVE}/{u}/"><div class="post__img"><img src="{r}assets/img/{img}" alt="" loading="lazy"></div>
<div class="post__body"><span class="post__meta">{cat} · {date}</span><h3>{t}</h3><p>{ex}</p></div></a>''' for u, cat, date, t, ex, img in items)


def enquiry_form(r):
    opts = "".join(f'<option>{s["name"]}</option>' for s in SERVICES[:7])
    return f'''<form class="form" data-enquiry novalidate>
<h3>Send us a message</h3><p>We'll get back to you quickly — usually the same day.</p>
<div class="form-grid">
  <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
  <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
  <div class="field full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
  <div class="field full"><fieldset><legend>How would you like to talk?</legend><div class="pills">
    <label><input type="radio" name="method" value="Phone call" checked><span>Phone call</span></label>
    <label><input type="radio" name="method" value="In person"><span>In person</span></label>
    <label><input type="radio" name="method" value="Email"><span>Email</span></label></div></fieldset></div>
  <div class="field full"><label for="f-topic">What can we help with?</label><select id="f-topic" name="topic"><option value="">Not sure yet</option>{opts}</select></div>
  <div class="field full"><label for="f-msg">Message <span style="font-weight:400;color:var(--muted)">(optional)</span></label><textarea id="f-msg" name="message"></textarea></div>
  <div class="field full"><label class="check"><input type="checkbox" name="newsletter"> Sign me up to the newsletter. You can opt out at any time.</label></div>
  <div class="field full"><label class="check"><input type="checkbox" name="consent" required> I agree to Oxley Mortgage Solutions using the data entered above to provide me with information about services offered and to respond to my enquiry.</label></div>
</div>
<button class="btn" type="submit">Send enquiry {ico("arrow")}</button>
<p class="form__status" role="status" aria-live="polite"></p>
</form>'''


def contact_section(r):
    return f'''<section class="section section--white" id="contact"><div class="wrap split split--top">
<div class="reveal"><span class="eyebrow">Talk to us</span><h2>Talk to us about your mortgage</h2>
<p class="lede">We're a specialist mortgage and protection firm built around personal service and straightforward advice. As a family-run business, we believe every client deserves time, clarity and solutions tailored to them.</p>
<p>Mortgages and protection can feel overwhelming, but we're here to simplify the process. We'll explain your options clearly, answer your questions honestly, and guide you at every stage.</p>
<ul class="checks"><li>Friendly, no-pressure initial discussion</li><li>Expert mortgage advisers</li><li>Experience with complex and non-standard cases</li><li>Advisers who go the extra mile</li></ul>
<div class="contact-options">
  <a class="contact-opt" href="{CAL_CALL}" target="_blank" rel="noopener"><span class="ico">{ico("phone")}</span><div><strong>Book a call</strong><br><span>30 minutes, at a time to suit you</span></div></a>
  <a class="contact-opt" href="{CAL_VISIT}" target="_blank" rel="noopener"><span class="ico">{ico("pin")}</span><div><strong>Meet in person</strong><br><span>At our Chesterfield office</span></div></a>
  <a class="contact-opt" href="mailto:{EMAIL}"><span class="ico">{ico("mail")}</span><div><strong>Send an email</strong><br><span>{EMAIL}</span></div></a>
</div></div>
<div class="reveal">{enquiry_form(r)}</div>
</div></section>
'''


# ---------- pages ----------

def home():
    r = ""
    stats = [("search", "1,000s of mortgages", "From high street to specialist lenders"),
             ("clock", "15 minute chat", "Same-day appointments available"),
             ("user", "1 dedicated adviser", "With you from first call to completion"),
             ("heart", "Family run", "Chesterfield-based, since 1997")]
    stat_html = "".join(f'<div class="stat"><span class="ico">{ico(i)}</span><div><strong>{a}</strong><span>{b}</span></div></div>' for i, a, b in stats)
    body = f'''<section class="hero"><div class="wrap">
  <div class="hero__copy">
    <span class="eyebrow">Chesterfield mortgage brokers</span>
    <h1>Making home ownership a reality</h1>
    <p class="hero__sub">Search <b>1,000s</b> of mortgages by spending <b>15</b> minutes talking to <b>1</b> adviser.</p>
    <p>Whether you're a first-time buyer, remortgaging, self-employed or dealing with adverse credit, we'll work hard to find the right solution for you.</p>
    <div class="btn-row"><a class="btn" href="{CAL_CALL}" target="_blank" rel="noopener">{ico("cal")}Book a call today</a><a class="btn btn--ghost" href="{TEL}">{ico("phone")}{PHONE}</a></div>
    <p class="hero__note">{ico("check")}Friendly, no-pressure first conversation · Same-day appointments</p>
  </div>
  <div class="hero__media">
    <img src="assets/img/team.webp" alt="Mat, George and Craig — the Oxley mortgage team" width="600" height="622" fetchpriority="high">
    <div class="hero__badge"><span class="rating__g" style="width:34px;height:34px;display:grid;place-items:center">{G_LOGO}</span><div><strong>Excellent</strong><span class="stars">★★★★★</span> 64 reviews</div></div>
  </div>
</div></section>
<section class="stats" aria-label="At a glance"><div class="wrap">{stat_html}</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">How we can help</span><h2>Mortgage advice for every situation</h2>
  <p class="lede">We work with a wide panel of lenders — including specialists who look beyond automated decisions — to find the right fit for you.</p></div>
  <div class="grid grid--4">{service_cards(r, SERVICES[:8])}</div>
</div></section>

<section class="section section--white"><div class="wrap split">
  <div class="photo-stack reveal"><div class="photo"><img src="assets/img/office-2.webp" alt="George giving a thumbs up" loading="lazy"></div><div class="photo photo--float"><img src="assets/img/couple-home.webp" alt="Happy couple in their new home" loading="lazy"></div></div>
  <div class="reveal"><span class="eyebrow">Why Oxley</span><h2>Straightforward mortgage advice you can trust</h2>
  <p class="lede">Finding the right mortgage shouldn't feel impossible.</p>
  <p>As a family-run brokerage, we take the time to understand your situation, cut through the jargon, and guide you with straight, honest advice — whether you're buying your first home, expanding your portfolio, or have been turned down elsewhere.</p>
  <p>At Oxley, you're never just another application. You get real people, real support, and a dedicated adviser who stays with you from the very first conversation through to completion.</p>
  <div class="btn-row"><a class="btn" href="about-oxley/">Meet the team {ico("arrow")}</a></div></div>
</div></section>

<section class="section section--navy"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Turned down elsewhere?</span><h2>Mortgages when the answer has been “no”</h2>
  <p class="lede" style="color:#d9d7ea">Not every application fits neatly into a box. If you've been declined by a bank, told your income doesn't stack up, or feel your circumstances are being misunderstood, you're not alone.</p></div>
  <div class="split split--top">
    <div><p>As specialist mortgage brokers we present your situation clearly to the right lenders, giving you the best possible chance of getting the mortgage you need. We regularly help with:</p>
    <ul class="checks"><li>Previous credit issues or missed payments</li><li>Self-employed or multiple income streams</li><li>Short trading history or limited accounts</li><li>Buy-to-let and investment property finance</li><li>First-time buyers needing extra guidance</li></ul></div>
    <div><div class="steps" style="grid-template-columns:1fr">
      <div class="step"><h3>Have a quick chat</h3><p>15 minutes on the phone or in person. We'll get to know you and your plans.</p></div>
      <div class="step"><h3>We search the market</h3><p>We compare lenders — including specialists you won't find on the high street.</p></div>
      <div class="step"><h3>We handle it to completion</h3><p>Your adviser deals with the paperwork and keeps you updated all the way to “YES”.</p></div>
    </div></div>
  </div>
</div></section>

{reviews()}

<section class="section"><div class="wrap">
  <div class="section-head section-head--center"><span class="eyebrow">Why homebuyers choose us</span><h2>Always working to get you that all-important “YES”</h2></div>
  {yes_grid()}
</div></section>

<section class="section section--white"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Meet the team</span><h2>Meet the mortgage simplifiers</h2><p class="lede">Decades of experience and thousands of happy clients.</p></div>
  {team_cards(r)}
</div></section>

<section class="section"><div class="wrap">
  <div class="reviews-head"><div><span class="eyebrow">Help &amp; guides</span><h2>Insight, help &amp; guides</h2></div><a class="btn btn--ghost" href="help-advice/">All articles {ico("arrow")}</a></div>
  <div class="grid grid--4">{posts(r, POSTS[:4])}</div>
</div></section>

{contact_section(r)}
{cta_band(r)}'''
    return page(r, "", "Oxley Mortgage Solutions | Mortgage Brokers in Chesterfield",
                "Expert mortgage advice for first-time buyers, remortgages, self-employed and bad credit cases. Find the right mortgage for you with Oxley Mortgage Solutions.", "", body)


def page_hero(r, eyebrow, h1, lede, img=None, crumbs=None):
    c = ""
    if crumbs:
        c = '<nav class="crumbs" aria-label="Breadcrumb"><a href="' + r + '">Home</a>' + "".join(f'<span>/</span><a href="{r}{u}">{t}</a>' if u else f'<span>/</span>{t}' for t, u in crumbs) + "</nav>"
    pic = f'<div class="page-hero__img"><img src="{r}assets/img/{img}" alt="" fetchpriority="high"></div>' if img else ""
    btns = f'<div class="btn-row" style="margin-top:24px"><a class="btn btn--yellow" href="{CAL_CALL}" target="_blank" rel="noopener">{ico("cal")}Book a call</a><a class="btn btn--ghost" href="{TEL}" style="color:#fff;border-color:rgba(255,255,255,.35)">{ico("phone")}{PHONE}</a></div>'
    return f'<section class="page-hero"><div class="wrap"><div>{c}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{lede}</p>{btns}</div>{pic}</div></section>'


def render_block(text):
    if text.startswith("@checks:"):
        return '<ul class="checks checks--2">' + "".join(f"<li>{x}</li>" for x in text[8:].split("|")) + "</ul>"
    if text.startswith("@notice:"):
        return f'<div class="notice">{ico("info")}<span>{text[8:]}</span></div>'
    return f"<p>{text}</p>"


def service(s):
    r = "../"
    prose = ""
    for h, paras in s["body"]:
        prose += (f"<h2>{h}</h2>" if h else "") + "".join(render_block(p) for p in paras)
    if s.get("faq"):
        prose += "<h2>Want to know more?</h2><div class='faq'>" + "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in s["faq"]) + "</div>"
    prose += f'<p style="margin-top:2em"><strong>If you\'re ready to take the next step, we\'re ready to help you get there.</strong></p><a class="btn" href="{CAL_CALL}" target="_blank" rel="noopener">{ico("cal")}Book an appointment today</a>'
    others = "".join(f'<li><a href="{r}{o["slug"]}/"{" aria-current=page" if o is s else ""}>{o["name"]} {ico("arrow")}</a></li>' for o in SERVICES)
    body = page_hero(r, "Mortgages", s["h1"], s["lede"], s["img"], [("Mortgages", "mortgages/"), (s["name"], None)]) + f'''
<section class="section"><div class="wrap content-grid">
  <article class="prose">{prose}</article>
  <aside class="aside">
    <div class="aside-card aside-card--navy"><h3>Speak to an adviser</h3><p>Friendly, no-pressure advice. Same-day appointments, Monday to Friday.</p>
      <a class="btn btn--yellow" href="{CAL_CALL}" target="_blank" rel="noopener">{ico("cal")}Book a call</a><a class="btn btn--ghost" href="{TEL}">{ico("phone")}{PHONE}</a></div>
    <div class="aside-card"><h3>Other mortgages</h3><ul>{others}</ul></div>
  </aside>
</div></section>
{reviews()}
{contact_section(r)}'''
    return page(r, s["slug"], f'{s["name"]} | Oxley Mortgage Solutions', s["blurb"], s["slug"] + "/", body)


def mortgages():
    r = "../"
    body = page_hero(r, "Your options", "Your mortgage options with Oxley",
                     "We're a team of mortgage specialists committed to finding the right mortgage for you and your specific requirements. Here are some of the areas we specialise in.", "couple-home.webp", [("Mortgages", None)]) + f'''
<section class="section"><div class="wrap"><div class="grid grid--4">{service_cards(r)}</div></div></section>
<section class="section section--white"><div class="wrap"><div class="section-head section-head--center"><span class="eyebrow">Why Oxley</span><h2>Why homebuyers choose Oxley</h2></div>{yes_grid()}</div></section>
{cta_band(r)}'''
    return page(r, "mortgages", "Mortgages | Oxley Mortgage Solutions", "Explore your mortgage options with Oxley Mortgage Solutions.", "mortgages/", body)


def about():
    r = "../"
    body = page_hero(r, "About us", "Meet Oxley Mortgages",
                     "We specialise in helping people secure the right mortgage — even if you've been turned down elsewhere. Oxley: your path to a “YES” made simple.", "office-1.webp", [("About Oxley", None)]) + f'''
<section class="section section--white"><div class="wrap">
  <div class="section-head"><span class="eyebrow">The team</span><h2>Meet the mortgage simplifiers</h2><p class="lede">Say hello to Oxley's dedicated team — decades of experience and thousands of happy clients.</p></div>
  {team_cards(r)}
</div></section>
<section class="section"><div class="wrap"><div class="section-head section-head--center"><span class="eyebrow">Why Oxley</span><h2>Why homebuyers choose Oxley</h2></div>{yes_grid()}</div></section>
{reviews()}
{contact_section(r)}'''
    return page(r, "about-oxley", "About Oxley | Oxley Mortgage Solutions", "Meet the family-run Oxley Mortgage Solutions team in Chesterfield.", "about-oxley/", body)


def help_advice():
    r = "../"
    body = page_hero(r, "Help &amp; Advice", "Insight, help &amp; guides",
                     "Free insights, help and guides from our mortgage experts — written in plain English.", None, [("Help &amp; Advice", None)]) + f'''
<section class="section"><div class="wrap"><div class="grid grid--3">{posts(r, POSTS)}</div></div></section>
{cta_band(r)}'''
    return page(r, "help-advice", "Help &amp; Advice | Oxley Mortgage Solutions", "Mortgage guides and advice from Oxley Mortgage Solutions.", "help-advice/", body)


def contact():
    r = "../"
    body = page_hero(r, "Contact", "Get in touch with Oxley",
                     "Whether you're a first-time buyer, remortgaging, or dealing with adverse credit, we'll work hard to find the right solution for you — even if you've been turned down elsewhere.", None, [("Contact", None)]) + f'''
{contact_section(r)}
<section class="section"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">Visit us</span><h2>Our Chesterfield office</h2>
  <address style="font-style:normal" class="lede">Unit 4, The Glass Yard<br>Sheffield Rd, Chesterfield<br>S41 8JY</address>
  <p><a href="{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a><br>Open Monday to Friday</p>
  <a class="btn" href="{CAL_VISIT}" target="_blank" rel="noopener">{ico("pin")}Book an in-person chat</a></div>
  <div class="photo reveal" style="aspect-ratio:4/3"><iframe title="Map of Oxley Mortgage Solutions office" src="https://www.google.com/maps?q=The+Glass+Yard,+Sheffield+Rd,+Chesterfield+S41+8JY&output=embed" style="border:0;width:100%;height:100%" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></section>'''
    return page(r, "contact-oxley-mortgages", "Contact | Oxley Mortgage Solutions", "Contact Oxley Mortgage Solutions in Chesterfield.", "contact-oxley-mortgages/", body)


def notfound():
    r = "/oxley/"
    body = page_hero(r, "404", "Sorry, we couldn't find that page", "Let's get you back on track.", None) + cta_band(r)
    return page(r, "", "Page not found | Oxley Mortgage Solutions", "Page not found", "", body)


def write(path, html):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(html)


if __name__ == "__main__":
    write("index.html", home())
    write("mortgages/index.html", mortgages())
    write("about-oxley/index.html", about())
    write("help-advice/index.html", help_advice())
    write("contact-oxley-mortgages/index.html", contact())
    for s in SERVICES:
        write(f'{s["slug"]}/index.html', service(s))
    write("404.html", notfound())
    print("built", 5 + len(SERVICES) + 1, "pages")
