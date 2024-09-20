CREATE TABLE IF NOT EXISTS policies(
    policy_id TEXT PRIMARY KEY,
    user_id TEXT DEFAULT NULL,
    status TEXT DEFAULT NULL,
    created_at DATE DEFAULT NULL,
    effective_date DATE DEFAULT NULL,
    canceled_date DATE DEFAULT NULL,
    renewal_date DATE DEFAULT NULL,
    annual_permium INTEGER DEFAULT NULL,
    tier DOUBLE PRECISION DEFAULT NULL,
    base_deductible INTEGER DEFAULT NULL,
    state TEXT DEFAULT NULL,
    perosnal_property_limit INTEGER DEFAULT NULL,
    personal_liability_limit INTEGER DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS users(
    user_id TEXT PRIMARY KEY,
    encrypted_password TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    language TEXT NOT NULL,
    timezone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS claims(
    claim_id TEXT PRIMARY KEY,
    user_id TEXT DEFAULT NULL,
    status TEXT DEFAULT NULL,
    submitted_date DATE DEFAULT NULL,
    closed_date DATE DEFAULT NULL,
    loss_type TEXT DEFAULT NULL,
    paid BOOLEAN DEFAULT NULL,
    paid_amount DOUBLE PRECISION DEFAULT NULL
);
