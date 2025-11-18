# MyBambu IMT Retention Strategy - EXECUTION PLAN
## 90-Day Sprint to Reduce Churn from 25.4% to 15%

**Date:** November 2025
**Teams:** Marketing, Strategy, BI/Analytics, Development
**Objective:** Save the business from death spiral by fixing retention

---

## 🎯 EXECUTIVE SUMMARY FOR LEADERSHIP

### The Situation
- **Current State:** Product is profitable (+$113K/month, 30.2% margin) but SHRINKING
- **The Problem:** 25.4% monthly churn = Death spiral (will shrink to 12K users in 3 months)
- **Root Cause:** Low LTV ($15.60) limits affordable CAC to $4.68 - cannot grow
- **The Solution:** Reduce churn to 15% → Increase LTV to $26.53 → Enable $7-8 CAC → Growth

### What We're Asking For
1. **Budget:** $70K for Q1 retention campaigns
2. **Headcount:** 1 Retention Manager (hire immediately)
3. **Development Resources:** 2 engineers for 90 days
4. **BI Resources:** 1 analyst for dashboards + churn prediction
5. **Marketing Resources:** Full team for 4 major campaigns

### Expected Results (90 Days)
- **Churn:** 25.4% → 15%
- **LTV Margin:** $15.60 → $26.53 (+70%)
- **Users:** Stabilize at 28K (vs death spiral to 12K)
- **Monthly Margin:** Maintain $111K (vs decline to $47K)
- **Affordable CAC:** $4.68 → $7.96 (+70%)
- **ROI:** $768K annual savings from avoided death spiral

---

## 📊 CRITICAL METRICS DASHBOARD (BI TEAM)

### Priority 1: Build These Dashboards THIS WEEK

#### 1. **Churn Prediction Dashboard** (Ship: Week 1)
**Purpose:** Identify at-risk users BEFORE they churn

**Data Points:**
- Days since last transaction
- Transaction frequency trend (increasing/decreasing)
- Average transaction size
- Corridor used (Mexico, Honduras, etc.)
- Payment method preference
- Failed transaction count
- Customer service contact history
- App engagement metrics (logins, browse-only sessions)

**Churn Risk Scoring:**
```sql
-- HIGH RISK (>60% chance to churn)
- No transaction in 21+ days
- Failed transaction in last 30 days
- Declining frequency (2+ txns down vs prior month)
- No app login in 14+ days

-- MEDIUM RISK (30-60% chance)
- No transaction in 14-20 days
- 1 failed transaction in last 60 days
- Flat frequency (no growth)
- 1 login per week

-- LOW RISK (<30% chance)
- Transaction in last 7 days
- Increasing frequency
- 3+ logins per week
```

**Output:** Daily CSV of at-risk users for marketing team

#### 2. **Retention Metrics Dashboard** (Ship: Week 1)
**KPIs to Track Daily:**
- Daily/Weekly/Monthly Churn Rate
- Cohort Retention Curves (by signup month)
- Win-back Campaign Performance
- Loyalty Program Enrollment & Tier Distribution
- Referral Program Activity
- VIP Program Retention vs Non-VIP

**Segments to Track:**
- New Users (0-30 days)
- Active Users (1+ txn in last 30 days)
- At-Risk Users (no txn in 14+ days)
- Churned Users (no txn in 60+ days)
- Win-back Users (reactivated after churn)

#### 3. **Campaign Performance Dashboard** (Ship: Week 2)
**For Each Campaign Track:**
- Impressions / Opens / Clicks
- Activation Rate (% who transact)
- Cost per Activation
- Revenue per Activated User
- ROI (Revenue - Cost) / Cost

**Campaigns:**
- Win-back Email Series
- Loyalty Program Emails
- Referral Program
- VIP Program Communications
- In-app Messages

#### 4. **Economics Dashboard** (Ship: Week 2)
**Track Weekly:**
- Total Revenue (FX + Fees)
- FX Revenue % of Total
- Rail Costs
- Gross Margin $
- Gross Margin %
- Revenue per Customer
- Margin per Customer
- LTV Margin (by churn rate)
- Affordable CAC

**Segment By:**
- Country
- Payment Method (Bank vs Cash)
- User Type (New, Active, At-Risk, VIP)

---

## 💻 DEVELOPMENT TEAM - TECHNICAL REQUIREMENTS

### Sprint 1 (Week 1-2): Foundation

#### 1.1 **Churn Data Pipeline** (Priority: CRITICAL)
**Owner:** BI + Dev
**Deadline:** Day 7

**Requirements:**
- Daily batch job to calculate churn risk scores
- Export to CSV/API for marketing automation
- Snowflake query optimization for performance
- Automated alerting if churn spikes >2%

**Deliverables:**
```python
# Example output
{
    "user_id": "12345",
    "email": "user@example.com",
    "phone": "+1234567890",
    "churn_risk": "HIGH",
    "risk_score": 0.78,
    "last_transaction_days": 28,
    "reason": "No transaction in 28 days + declining frequency",
    "recommended_action": "win_back_campaign"
}
```

#### 1.2 **Loyalty Program Infrastructure** (Priority: HIGH)
**Owner:** Dev Team
**Deadline:** Day 14

**Requirements:**
- Tier assignment logic (Regular, Frequent, Power)
- FX discount calculation engine
- Tier badge display in app
- Push notification system for tier upgrades

**Tiers:**
- **Regular:** 4-6 txns/month → 0.1% FX discount
- **Frequent:** 7-9 txns/month → 0.2% FX discount + priority support
- **Power:** 10+ txns/month → 0.3% FX discount + instant transfers

**API Endpoints:**
```javascript
GET /api/v1/loyalty/tier
POST /api/v1/loyalty/apply-discount
GET /api/v1/loyalty/progress
```

#### 1.3 **Referral Program System** (Priority: HIGH)
**Owner:** Dev Team
**Deadline:** Day 14

**Requirements:**
- Unique referral code generation
- Referral tracking (code usage)
- $5 credit issuance automation
- In-app referral sharing (SMS, WhatsApp, Email)
- Fraud prevention (limit 1 referral per phone number)

**User Flow:**
1. User gets unique code in app
2. Shares via SMS/WhatsApp
3. New user signs up with code
4. Both users get $5 credit automatically
5. Credit applied to next transaction

### Sprint 2 (Week 3-4): Campaign Infrastructure

#### 2.1 **In-App Messaging System** (Priority: MEDIUM)
**Owner:** Dev Team
**Deadline:** Day 21

**Features:**
- Banner messages on home screen
- Modal popups for important campaigns
- Dismissible/persistent options
- A/B testing support
- Analytics tracking (impressions, clicks, conversions)

**Use Cases:**
- Win-back offers for at-risk users
- Loyalty tier upgrade notifications
- Referral program promotion
- VIP program invitations

#### 2.2 **VIP Program Features** (Priority: MEDIUM)
**Owner:** Dev Team
**Deadline:** Day 28

**Features:**
- VIP badge in app
- Priority support chat (flag in Zendesk/Intercom)
- Instant transfer toggle (if feasible)
- Dedicated VIP phone number
- Monthly VIP newsletter

**VIP Criteria:**
- Top 10% by volume (2,855 users)
- 10+ transactions/month OR
- $2,000+ monthly volume

### Sprint 3 (Week 5-6): Optimization

#### 3.1 **A/B Testing Framework** (Priority: MEDIUM)
**Owner:** Dev Team
**Deadline:** Day 35

**Capabilities:**
- Test different offer amounts ($5 vs $10 credit)
- Test messaging variations
- Test discount levels
- Cohort assignment (50/50 split)
- Statistical significance calculation

#### 3.2 **Push Notification Engine** (Priority: MEDIUM)
**Owner:** Dev Team
**Deadline:** Day 42

**Triggers:**
- No transaction in 14 days → "We miss you" message
- Tier upgrade → "Congrats! You're now Frequent tier"
- Referral success → "Your friend joined! Here's $5"
- Failed transaction → "Need help? Here's support"

---

## 📢 MARKETING TEAM - CAMPAIGN EXECUTION

### Campaign 1: WIN-BACK (Launch: Week 1)

#### Target Audience
- **Churned Users:** No transaction in 45-90 days (7,096 users from Oct)
- **At-Risk Users:** No transaction in 21-44 days (est. 5,000 users)

#### Campaign Structure

**Email Series (7 emails over 28 days):**

1. **Day 1 - "We Miss You"**
   - Subject: "¿Nos extrañas? Get 1 FREE transaction"
   - Offer: Waive ALL fees on next transaction (FX spread + transaction fee)
   - CTA: "Send Money Now"
   - Estimated cost: $3.52/user (avg revenue per txn)

2. **Day 3 - Social Proof**
   - Subject: "28,000 people sent money home last month"
   - Content: Customer testimonials, success stories
   - Offer reminder: Free transaction expires in 25 days

3. **Day 7 - Urgency**
   - Subject: "⏰ Your FREE transaction expires in 21 days"
   - Content: Countdown timer, reminder of offer
   - CTA: "Claim My Free Transaction"

4. **Day 14 - Pain Point**
   - Subject: "Sending money shouldn't be complicated"
   - Content: How MyBambu makes it easy vs competitors
   - Offer reminder: Free transaction expires in 14 days

5. **Day 21 - Final Reminder**
   - Subject: "🔔 LAST CHANCE: Free transaction expires in 7 days"
   - Content: Strong urgency, countdown
   - CTA: "Send Money FREE Today"

6. **Day 24 - FINAL PUSH**
   - Subject: "⚠️ Your FREE $3.50 expires in 3 days!"
   - Content: Dollar amount (make it tangible)
   - CTA: "Don't Lose Your Free Money"

7. **Day 28 - Last Email**
   - Subject: "This is goodbye... unless you want 50% off?"
   - Offer: Last chance - 50% off transaction fee (smaller offer)
   - CTA: "Get 50% Off Now"

**SMS Series (3 messages):**
- Day 1: "We miss you! Get 1 FREE transaction: [link]"
- Day 14: "14 days left for your FREE transaction: [link]"
- Day 27: "LAST DAY for FREE transaction: [link]"

**Budget:**
- Email: $0 (existing tool)
- SMS: 12,096 users × 3 messages × $0.02 = $726
- Offer cost: 20% activation × 12,096 × $3.52 = $8,515
- **Total: $9,241**

**Expected Results:**
- Activation Rate: 15-20%
- Reactivated Users: 1,800-2,400
- Cost per Reactivation: $3.85-$5.13
- LTV: $15.60 × 1,800 = $28,080
- **ROI: 203%**

#### Campaign 2: LOYALTY PROGRAM (Launch: Week 2)

#### Announcement Phase (Week 2-3)

**Email Announcement:**
- Subject: "🎉 Introducing MyBambu Rewards - Earn while you send!"
- Content:
  - Explain 3 tiers (Regular, Frequent, Power)
  - Show benefits at each tier
  - "You're already Regular tier!"
  - Progress bar to next tier
- CTA: "Check My Tier"

**In-App Banner:**
- "New: MyBambu Rewards! Earn discounts on every transaction →"

**SMS Announcement:**
- "Good news! You're earning rewards with every transaction. Check your tier: [link]"

#### Tier Communication (Ongoing)

**Tier Upgrade Notifications:**
```
Push Notification:
"🎉 Congrats! You're now FREQUENT tier"
"You've unlocked 0.2% FX discount + priority support!"
[Button: See Benefits]

Email:
Subject: "You just unlocked FREQUENT tier rewards!"
Content:
- What you unlocked
- How much you're saving per transaction
- How to reach Power tier
- CTA: "Send Money & Save Now"
```

**Monthly Tier Summary:**
```
Email (sent 1st of month):
Subject: "Your November Rewards Summary"

Content:
- Total saved this month: $XX.XX
- Current tier: Frequent
- Transactions to next tier: 3 more
- Projected savings if you reach Power: $YY.YY
- CTA: "Keep Earning Rewards"
```

**Budget:**
- Development: $0 (covered in dev sprint)
- Discount cost: $5,000/month (0.1-0.3% FX discounts)
- Email/SMS: $0 (automated)
- **Total: $5,000/month = $15,000 Q1**

**Expected Results:**
- Enrollment: 95%+ (automatic)
- Churn reduction: 25% → 20% (5% improvement)
- Monthly margin saved: ~$20K

#### Campaign 3: REFERRAL PROGRAM (Launch: Week 4)

#### Announcement Phase (Week 4)

**Email:**
- Subject: "Give $5, Get $5 - Share MyBambu with friends!"
- Content:
  - How it works
  - Your unique code
  - Share buttons (WhatsApp, SMS, Email)
- CTA: "Share & Earn $5"

**In-App:**
- Prominent "Refer & Earn" section
- Share flow:
  1. Tap "Invite Friends"
  2. Choose share method (WhatsApp/SMS/Email)
  3. Pre-filled message: "Send money home easier with MyBambu. Use my code XXXX and we both get $5! [link]"

**SMS:**
- "Want $5? Invite friends to MyBambu and you both get $5 credit: [link]"

#### Ongoing Promotion (Week 5-12)

**Monthly Leaderboard:**
```
Email (monthly):
Subject: "🏆 You've referred 3 friends - You're in the top 10%!"

Content:
- Your referral count: 3
- Your total earned: $15
- Top referrers this month
- Special prize for #1 (extra $50 bonus)
- CTA: "Refer More Friends"
```

**Referral Success Notifications:**
```
Push Notification:
"🎉 Your friend Maria just signed up! You both got $5"

Email:
Subject: "You just earned $5! Keep sharing"
Content:
- Friend's first name
- Your $5 credit added
- Total referrals: X
- CTA: "Invite More Friends"
```

**Budget:**
- $10 per successful referral
- Target: 5,000 referrals in Q1
- **Total: $50,000**

**Expected Results:**
- Referral rate: 10-15% of active users
- New users: 5,000
- Cost: $10 each ($50K total)
- LTV: $15.60 × 5,000 = $78,000
- **ROI: 56%**

#### Campaign 4: VIP PROGRAM (Launch: Week 5)

#### Invitation Phase (Week 5)

**VIP Invitation Email:**
```
Subject: "You're invited: Join MyBambu VIP"

Content:
Dear [Name],

You're one of our top 10% customers, and we want to show our appreciation.

You're invited to join MyBambu VIP:
✓ 0.3% FX discount on every transaction
✓ Priority customer support (dedicated line)
✓ Instant transfers (no waiting)
✓ Exclusive perks & early access to new features

This is invitation-only. Accept now:
[Accept VIP Invitation]

Best regards,
The MyBambu Team

P.S. You've saved $XX.XX with us. As VIP, you'd save $YY.YY more per month.
```

**VIP Welcome Email (upon acceptance):**
```
Subject: "Welcome to MyBambu VIP 🌟"

Content:
- VIP benefits overview
- Dedicated support number: 1-800-VIP-BAMB
- How to use instant transfers
- Monthly VIP newsletter signup
- CTA: "Start Saving More Today"
```

#### VIP Monthly Newsletter (Starting Week 6)

**Content:**
- Your monthly savings as VIP
- Exclusive feature previews
- VIP-only promotions
- Personal account manager introduction (if scaling)

**Budget:**
- Discounts: ~$3,000/month (0.3% on high-volume users)
- Support: $0 (priority queue in existing system)
- **Total: $3,000/month = $9,000 Q1**

**Expected Results:**
- VIP retention: 85-90% (vs 75% for non-VIP)
- High-value users saved: 428 users
- Margin saved: $15.7K/month = $47.1K Q1

---

## 📈 BI TEAM - ANALYTICS & REPORTING

### Week 1 Priorities

#### 1. **Cohort Analysis**
**Deliverable:** Excel/Tableau showing retention curves

**Analysis:**
- Cohort users by signup month (Jan 2024 - Oct 2025)
- Calculate retention at 30/60/90/180/365 days
- Identify best/worst performing cohorts
- Determine what changed (product changes, campaigns, etc.)

**Output:** "Users who signed up in March 2025 had 82% retention at 30 days vs 68% in October"

#### 2. **Churn Reason Analysis**
**Deliverable:** Report on why users churn

**Method:**
- Segment churned users by:
  - Failed transaction count
  - Customer support tickets
  - Average transaction size
  - Corridor used
  - Payment method
  - Days to first churn

**Hypothesis Testing:**
- Do users with failed transactions churn more? (YES - test this)
- Do smaller transaction users churn more?
- Do specific corridors have higher churn?

**Output:** "Users with 1+ failed transactions have 42% churn vs 23% without failures"

#### 3. **Segment Performance**
**Deliverable:** Dashboard showing economics by segment

**Segments:**
- By Country (MX, HN, NI, VE, CO, etc.)
- By Payment Method (Bank vs Cash)
- By Transaction Frequency (1-3, 4-6, 7-9, 10+ txns/month)
- By User Type (New, Active, At-Risk, Churned, VIP)

**Metrics:**
- Revenue per User
- Margin per User
- LTV by segment
- Churn by segment

**Output:** "Nicaragua users have $4.50 margin/txn (highest) vs Panama $0.80 (lowest)"

### Week 2-4 Priorities

#### 4. **A/B Test Analysis Framework**
**Deliverable:** Statistical testing for campaigns

**Tests to Run:**
- Win-back offer: $0 fee vs 50% off vs $5 credit
- Email subject lines: Urgency vs Social Proof vs FOMO
- Referral amount: $5 vs $10 vs $15
- Loyalty discount: 0.1% vs 0.2% vs 0.3%

**Analysis:**
- Sample size calculation
- Statistical significance (p-value < 0.05)
- Confidence intervals
- Winner determination

#### 5. **Predictive Churn Model**
**Deliverable:** Machine learning model for churn prediction

**Features:**
- Transaction frequency (last 7/14/30/60 days)
- Days since last transaction
- Failed transaction count
- Transaction amount trend
- Customer support interactions
- App engagement metrics

**Model:**
- Logistic regression OR
- Random forest OR
- XGBoost

**Output:** Churn probability score 0-100 for each user daily

#### 6. **Campaign Attribution**
**Deliverable:** Dashboard showing which campaigns drive revenue

**Tracking:**
- UTM parameters in all links
- Campaign codes in transactions
- First-touch attribution (what brought them back)
- Last-touch attribution (what drove conversion)

**Output:** "Win-back email drove 1,200 transactions = $45K revenue at $9K cost = 400% ROI"

---

## 🎯 STRATEGY TEAM - PROGRAM MANAGEMENT

### Week-by-Week Execution Plan

#### WEEK 1 (Days 1-7)
**Theme:** Foundation & Launch Win-back

**Monday (Day 1):**
- ✅ All-hands kickoff meeting (this meeting!)
- ✅ Assign roles & responsibilities
- ✅ Dev team starts churn data pipeline
- ✅ BI team starts cohort analysis

**Tuesday (Day 2):**
- ✅ Marketing drafts win-back email series
- ✅ Legal reviews email content & offers
- ✅ BI team pulls churned user list (7,096 users)

**Wednesday (Day 3):**
- ✅ Marketing finalizes email creative
- ✅ Dev team builds email templates
- ✅ Set up email automation in tool (Braze/SendGrid/etc.)

**Thursday (Day 4):**
- ✅ Internal test of email series
- ✅ QA email links, offer codes
- ✅ BI team delivers retention dashboard

**Friday (Day 5):**
- ✅ Final approval from leadership
- ✅ Marketing loads user list
- ✅ Schedule email send for Monday

**Weekend:**
- Dev team finishes churn data pipeline
- BI team analyzes cohort data

**Sunday (Day 7):**
- 🚀 **LAUNCH: Win-back Email #1 sent to 12,096 users**
- Monitor open rates, click rates, activations

**Metrics to Track:**
- Open rate (target: 25%+)
- Click rate (target: 10%+)
- Activation rate (target: 15%+)

#### WEEK 2 (Days 8-14)
**Theme:** Loyalty Program Launch

**Monday (Day 8):**
- ✅ Review win-back campaign performance
- ✅ Optimize email 2-7 based on data
- ✅ Dev team starts loyalty program infrastructure

**Tuesday-Wednesday (Days 9-10):**
- ✅ Marketing creates loyalty program creative
- ✅ Design tier badges for app
- ✅ Write tier benefit descriptions

**Thursday (Day 11):**
- ✅ Dev team delivers tier assignment logic
- ✅ QA loyalty program in staging

**Friday (Day 12):**
- ✅ Final QA & testing
- ✅ Marketing prepares launch emails

**Weekend (Days 13-14):**
- ✅ Deploy loyalty program to production
- ✅ Assign all users to tiers

**Sunday (Day 14):**
- 🚀 **LAUNCH: Loyalty Program Announcement Email**
- 🚀 **LAUNCH: In-app loyalty badges live**

**Metrics to Track:**
- Tier distribution (% in each tier)
- App engagement lift
- Transaction frequency increase

#### WEEK 3 (Days 15-21)
**Theme:** Referral Program Build

**Monday (Day 15):**
- ✅ Review win-back + loyalty performance
- ✅ Dev team starts referral program
- ✅ Generate unique codes for all users

**Tuesday-Thursday (Days 16-18):**
- ✅ Build referral tracking system
- ✅ Create referral landing page
- ✅ Build share flow in app (WhatsApp/SMS/Email)

**Friday (Day 19):**
- ✅ QA referral system
- ✅ Test $5 credit issuance
- ✅ Marketing creates referral campaign creative

**Weekend (Days 20-21):**
- ✅ Final testing of referral flows
- ✅ Set up fraud prevention rules

**Monday (Day 22):**
- 🚀 **LAUNCH: Referral Program** (planned for Week 4)

#### WEEK 4 (Days 22-28)
**Theme:** Referral Program Launch & VIP Planning

**Monday (Day 22):**
- 🚀 **LAUNCH: Referral Program Announcement**
- Monitor referral code usage
- Track activation rates

**Tuesday-Friday (Days 23-26):**
- ✅ Dev team builds VIP features
- ✅ BI team identifies top 10% users (2,855)
- ✅ Marketing creates VIP invitation emails
- ✅ Set up VIP support phone number/queue

**Weekend (Days 27-28):**
- ✅ QA VIP program
- ✅ Finalize VIP invitation list

#### WEEK 5-6 (Days 29-42)
**Theme:** VIP Launch & Optimization

**Day 29:**
- 🚀 **LAUNCH: VIP Program Invitations**

**Days 30-42:**
- Monitor VIP acceptance rate
- Track VIP retention vs non-VIP
- A/B test campaign variations
- Optimize email send times
- Review churn progress weekly

**Key Milestone (Day 42):**
- Review 6-week results
- Churn target: <22% (from 25.4%)
- Make go/no-go decision on price increases

#### WEEK 7-12 (Days 43-90)
**Theme:** Optimization & Scale

**Focus:**
- Double down on winning campaigns
- Kill underperforming campaigns
- A/B test new variations
- Expand referral program incentives
- Add new loyalty tier benefits

**Key Milestones:**
- Day 60: Review churn (target: <18%)
- Day 90: Final review (target: <15%)

---

## 💰 BUDGET BREAKDOWN

### Q1 Investment: $70,000

| Campaign | Month 1 | Month 2 | Month 3 | Total Q1 |
|----------|---------|---------|---------|----------|
| **Win-back** | $9,000 | $2,000 | $2,000 | $13,000 |
| **Loyalty Program** | $5,000 | $5,000 | $5,000 | $15,000 |
| **Referral Program** | $10,000 | $20,000 | $20,000 | $50,000 |
| **VIP Program** | $0 | $3,000 | $3,000 | $6,000 |
| **SMS/Email Tools** | $500 | $500 | $500 | $1,500 |
| **Analytics Tools** | $1,000 | $0 | $0 | $1,000 |
| **Contingency** | $1,500 | $1,500 | $1,500 | $4,500 |
| **TOTAL** | $27,000 | $32,000 | $32,000 | **$91,000** |

**Revised Budget: $91K** (originally estimated $70K - adjust accordingly)

---

## 📊 SUCCESS METRICS & KPIs

### North Star Metric
**Monthly Churn Rate**
- Current: 25.4%
- Month 1 Target: <22%
- Month 2 Target: <18%
- Month 3 Target: <15%
- Long-term Target: <12%

### Tier 1 Metrics (Review Daily)
1. **Churn Rate** - Must hit targets above
2. **Win-back Activation Rate** - Target: 15%+
3. **Referral Conversion Rate** - Target: 8%+
4. **Gross Margin** - Maintain $110K+

### Tier 2 Metrics (Review Weekly)
5. **LTV Margin** - Track movement toward $26+
6. **Active Users** - Stabilize at 28K+
7. **Transaction Frequency** - Increase 3.73 → 4.5+
8. **VIP Retention Rate** - Target: 85%+

### Tier 3 Metrics (Review Monthly)
9. **Campaign ROI** - Each campaign must be profitable
10. **CAC** - Should stay under affordable level
11. **Customer Satisfaction (CSAT)** - Don't sacrifice quality
12. **Net Promoter Score (NPS)** - Track brand health

---

## ⚠️ RISK MITIGATION

### Risk 1: Campaigns Don't Reduce Churn
**Probability:** Medium
**Impact:** Critical (death spiral continues)

**Mitigation:**
- A/B test every campaign before full launch
- Start with small cohorts (500-1,000 users)
- Have 3 backup campaign ideas ready
- Monitor results daily, pivot fast
- Survey churned users to understand why

**Trigger:** If churn not at 22% by Day 30, escalate to CEO

### Risk 2: Budget Overruns
**Probability:** Low
**Impact:** Medium

**Mitigation:**
- Set hard caps on referral program ($50K max)
- Monitor spend weekly
- Pre-approve all new campaigns
- 10% contingency buffer built in

**Trigger:** If >90% budget spent by Day 60, pause new campaigns

### Risk 3: Technical Delays
**Probability:** Medium
**Impact:** High (delays campaign launches)

**Mitigation:**
- Have manual workarounds ready
- CSV exports instead of API if needed
- Use existing tools (email platform) as backup
- Bi-weekly sprint reviews

**Trigger:** If dev milestones miss by >7 days, escalate

### Risk 4: Margins Decline
**Probability:** Low
**Impact:** Critical

**Mitigation:**
- Monitor gross margin weekly
- Discounts have caps (max 0.3%)
- Win-back offers are time-limited
- If margin drops below $100K for 2 weeks, reduce discounts

**Trigger:** Margin <$100K for 2 consecutive weeks = emergency review

### Risk 5: User Backlash
**Probability:** Very Low
**Impact:** Medium

**Mitigation:**
- All campaigns are positive (rewards, not penalties)
- No price increases during retention push
- Customer support trained on new programs
- Monitor social media & app reviews

**Trigger:** App rating drops below 4.0 = pause campaigns

---

## 🎬 DECISION POINTS

### Week 2 Decision: Continue or Pivot Win-back?
**Question:** Is win-back campaign working?

**Go Criteria:**
- Activation rate >10%
- Open rate >20%
- Cost per reactivation <$8

**No-Go Action:**
- Test different offer ($10 credit vs free fee)
- Change messaging (urgency vs benefit)
- Try different channel (SMS vs email)

### Week 6 Decision: Price Increase?
**Question:** Should we raise bank payout fee from $0.85 to $1.25?

**Go Criteria:**
- Churn <22%
- User sentiment stable (NPS >30)
- Competitive analysis shows we're still best price

**No-Go Action:**
- Wait until Month 3
- Focus on retention first

### Week 9 Decision: Scale or Optimize?
**Question:** Scale winning campaigns or optimize existing?

**Scale Criteria:**
- All campaigns ROI positive
- Churn <18%
- LTV margin >$22

**Optimize Criteria:**
- Any campaign ROI <50%
- Churn still >18%
- Run more A/B tests before scaling

### Week 12 Decision: Year 2 Strategy
**Question:** What's the H1 2026 plan?

**Options:**
1. **Aggressive Growth** (if churn <15%)
   - Increase CAC to $8
   - Launch paid acquisition
   - Expand to new corridors

2. **Continued Optimization** (if churn 15-18%)
   - Keep retention focus
   - Incremental improvements
   - Delay growth

3. **Crisis Mode** (if churn still >20%)
   - Emergency measures
   - Consider product changes
   - Re-evaluate business model

---

## 📞 TEAM ROLES & RESPONSIBILITIES

### Strategy Lead (You)
- **Overall coordination** of 90-day sprint
- Weekly progress reviews with all teams
- Executive reporting (CEO, CFO updates)
- Budget management
- Risk escalation
- Go/no-go decisions at decision points

### Marketing Team Lead
**Responsibilities:**
- Campaign creative development
- Email/SMS copywriting
- Campaign execution & monitoring
- A/B test management
- User segmentation coordination with BI
- Customer communication calendar

**Deliverables:**
- Week 1: Win-back campaign live
- Week 2: Loyalty announcement live
- Week 4: Referral campaign live
- Week 5: VIP invitations sent
- Weekly: Performance reports

### BI/Analytics Lead
**Responsibilities:**
- Dashboard development (4 dashboards)
- Churn prediction model
- Cohort analysis
- A/B test analysis
- Campaign attribution
- Weekly metrics reporting

**Deliverables:**
- Day 7: Churn prediction dashboard
- Day 7: Retention metrics dashboard
- Day 14: Campaign performance dashboard
- Day 14: Economics dashboard
- Day 30: Predictive churn model
- Weekly: Metrics report to leadership

### Development Team Lead
**Responsibilities:**
- Feature development (loyalty, referral, VIP)
- API integrations
- Data pipeline maintenance
- QA & testing
- Production deployment
- Bug fixes & support

**Deliverables:**
- Day 7: Churn data pipeline
- Day 14: Loyalty program features
- Day 14: Referral program system
- Day 28: VIP program features
- Day 35: A/B testing framework
- Day 42: Push notification engine

---

## 📅 MEETING STRUCTURE

### Daily Standups (15 min)
**Who:** Strategy + Marketing + BI + Dev leads
**When:** 9:00 AM daily
**Format:**
- What did you do yesterday?
- What are you doing today?
- Any blockers?

### Weekly Sprint Reviews (60 min)
**Who:** All teams + Leadership
**When:** Every Monday 10:00 AM
**Agenda:**
1. Metrics review (churn, campaigns, margin)
2. Last week accomplishments
3. This week priorities
4. Risks & escalations
5. Budget status

### Bi-weekly Sprint Planning (90 min)
**Who:** All teams
**When:** Every other Friday 2:00 PM
**Agenda:**
1. Review last 2 weeks
2. Plan next 2 weeks
3. Prioritize backlog
4. Resource allocation
5. Timeline adjustments

---

## 🎯 CALL TO ACTION FOR THIS MEETING

By the end of this meeting, we need:

### ✅ Decisions Made:
1. [ ] Approve $91K budget for Q1
2. [ ] Approve hiring 1 Retention Manager
3. [ ] Allocate 2 engineers for 90 days
4. [ ] Allocate 1 BI analyst for dashboards
5. [ ] Confirm all team leads assigned

### ✅ Actions Assigned:
1. [ ] **Marketing:** Draft win-back emails by EOD tomorrow
2. [ ] **BI:** Pull churned user list (7,096) by EOD today
3. [ ] **Dev:** Start churn data pipeline tomorrow morning
4. [ ] **Strategy:** Schedule daily standups starting tomorrow
5. [ ] **HR:** Post Retention Manager job by EOD this week

### ✅ Timeline Confirmed:
1. [ ] Day 7: Win-back campaign launches
2. [ ] Day 14: Loyalty program launches
3. [ ] Day 28: Referral program launches
4. [ ] Day 35: VIP program launches
5. [ ] Day 90: Review results & plan H1 2026

---

## 📚 APPENDIX

### A. Email Templates (Win-back Series)
See separate Google Doc: [Link to templates]

### B. Loyalty Program Rules
See separate document: [Link to rules]

### C. Referral Program Terms
See separate document: [Link to T&C]

### D. VIP Program Benefits
See separate document: [Link to benefits]

### E. SQL Queries for Dashboards
See separate document: [Link to queries]

---

**END OF EXECUTION PLAN**

**Next Step:** Review this plan in team meeting, assign owners, and LAUNCH Day 1 tomorrow.

Good luck! 🚀
