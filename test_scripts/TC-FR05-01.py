Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-05: Sections Inclusion/Exclusion for Campaign Pages', () => {
    before(async () => { await browser.url('http://www.ipsy.com/admin/campaign-config'); });
    it('Positive - Verify that sections can be included or excluded for a campaign landing page', async () => {
        const configInterface = await $('.config-interface');
        await expect(configInterface).toBeDisplayed();
        const sectionCheckbox = await $('.section-checkbox');
        await sectionCheckbox.click();
        const saveButton = await $('.save-config');
        await saveButton.click();
        const preview = await $('.preview');
        await expect(preview).toBeDisplayed();
    });
    it('Negative - Verify save fails if no sections selected', async () => {
        const sectionCheckbox = await $('.section-checkbox');
        await sectionCheckbox.click();
        const saveButton = await $('.save-config');
        await saveButton.click();
        const errorMessage = await $('.error-message');
        await expect(errorMessage).toBeDisplayed();
    });
    it('Edge - Verify with all sections included', async () => {
        const allCheckboxes = await $$  ('.section-checkbox');
        for (const checkbox of allCheckboxes) {
            await checkbox.click();
        }
        const saveButton = await $('.save-config');
        await saveButton.click();
        const preview = await $('.preview');
        await expect(preview).toBeDisplayed();
    });
});
